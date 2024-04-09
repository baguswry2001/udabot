import requests
import json
import re
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = input("Masukan Link video : ")
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
current_url = response.url
def extract_video_id(url):
    pattern = r'/video/(\d+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None 
IdVideo = extract_video_id(current_url)
hasil = IdVideo
url = "https://tiktok82.p.rapidapi.com/getVideoComments"
querystring = {f"video_id":hasil}
headers = {
    "X-RapidAPI-Key": "52085e5519mshde8a01821852f2ep1a5a1ejsn91497279f385",
    "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
if response.status_code == 200:
    formatted_response = json.dumps(response.json(), indent=4)
    data = json.loads(formatted_response)


    comments = data["data"]["comments"]
    table_data = []

    for comment in comments:
        text = comment["text"]
        user = comment["user"]["nickname"]
        table_data.append([user, text])

    print(tabulate(table_data, headers=["Username", "komentar"], tablefmt="grid"))
else:
    print("Gagal mendapatkan respons:", response.status_code)





