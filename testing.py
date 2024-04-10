


import requests
import json
import re
from bs4 import BeautifulSoup
from tabulate import tabulate

def extract_video_id(url):
    pattern = r'/video/(\d+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None 

url = input("Masukan Link video : ")
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
current_url = response.url

IdVideo = extract_video_id(current_url)
url = "https://tiktok82.p.rapidapi.com/getVideoComments"

headers = {
    "X-RapidAPI-Key": "52085e5519mshde8a01821852f2ep1a5a1ejsn91497279f385",
    "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
}

table_data = []
num_comments = 0

while True:
    querystring = {"video_id": IdVideo}
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        formatted_response = json.dumps(response.json(), indent=4)
        data = json.loads(formatted_response)
        comments = data["data"]["comments"]
        
        for comment in comments:
            text = comment["text"]
            user = comment["user"]["nickname"]
            table_data.append([user, text])
            num_comments += 1
            
        if not data.get("has_more") or num_comments >= 40:
            break
            
    else:
        print("Gagal mendapatkan respons:", response.status_code)
        break

print(tabulate(table_data[:40], headers=["Username", "komentar"], tablefmt="grid"))
