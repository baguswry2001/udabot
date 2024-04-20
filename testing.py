# import requests
# import json

# url = "https://tiktok82.p.rapidapi.com/getProfile"

# querystring = {"username":"ksbzhxjssvxvxv"}

# headers = {
#     "X-RapidAPI-Key": "52085e5519mshde8a01821852f2ep1a5a1ejsn91497279f385",
#     "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# # Memeriksa apakah respons berhasil
# if response.status_code == 200:
#     # Mengonversi respons ke format JSON
#     data = response.json()
    
#     # Mengonversi data menjadi string JSON yang terformat dengan baik
#     formatted_json = json.dumps(data, indent=4)
    
#     # Menampilkan hasil
#     print(formatted_json)
# else:
#     print("Failed to fetch data. Status code:", response.status_code)


import barcode
from barcode.writer import ImageWriter
def generate_barcode(text, filename):
    # Generate barcode object
    code128 = barcode.get_barcode_class('code128')
    barcode_instance = code128(text, writer=ImageWriter())

    # Save barcode image to file
    barcode_instance.save(filename)

def main():
    # Baca teks dari file
    with open('data.txt', 'r') as file:
        text = file.read().strip()

    # Generate barcode dari teks
    output_filename = 'barcode.png'
    generate_barcode(text, output_filename)
    print(f"Barcode telah dibuat dan disimpan sebagai '{output_filename}'")

if __name__ == "__main__":
    main()

