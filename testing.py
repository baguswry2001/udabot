# import requests
# import json

# url = "https://tiktok82.p.rapidapi.com/getVideoComments"

# querystring = {"video_id":"7352521444531637509"}

# headers = {
#     "X-RapidAPI-Key": "52085e5519mshde8a01821852f2ep1a5a1ejsn91497279f385",
#     "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# # Cek apakah respons berhasil
# if response.status_code == 200:
#     # Memformat respons JSON agar lebih mudah dibaca
#     formatted_response = json.dumps(response.json(), indent=4)
#     print(formatted_response)
# else:
#     print("Gagal mendapatkan respons:", response.status_code)
from colorama import init, Fore
from tabulate import tabulate
from colorama import init, Fore
from colorama import Fore, Back, Style
from pyfiglet import Figlet
def print_colored(text, color=Fore.WHITE, bg_color=Back.BLACK):
    print(bg_color + color + text + Style.RESET_ALL) 

def TiktokTools():
    print(Fore.CYAN , "          ;++xx     ")
    print(Fore.CYAN , "          ;X$$Xx    ")
    print(Fore.CYAN , "          ;X$$$$X;  ")
    print(Fore.CYAN , "          ;X$$$$$$$x")
    print(Fore.CYAN , "   ;;;;;x ;X$XxxXXXx")
    print(Fore.CYAN , ";;$$Xxxxx+;X$Xx     ")
    print(Fore.CYAN , ";X$Xxx    ;X$Xx     ")
    print(Fore.CYAN , ";X$Xx    ;;X$Xx     ")
    print(Fore.CYAN , ";X$$$X;;;;x$$xx     ")
    print(Fore.CYAN , " ;X$$$$$$$$Xxx      ")
    print(Fore.CYAN , "    xxXXxxxx     ")
    header = "+----------------------+"
    print(header)
    print_colored("|    TIKTIOK TOOLS     |", Fore.WHITE, Back.BLUE)
    print(header)
    
    
    from tabulate import tabulate

    headers = ["NO", "TOOLS",]
    data = [
        [1, "Tiktok download video"],
        [2,"Tiktok download video no watermark ( logo )"],
        [8, "Tiktok download all video frome profile"],
        [6, "Tiktok audio download"],
        [3, "Tiktok comment video generate"],
        [4, "Tiktok coment video generate + identity "],
        [5, "Tiktok user profile info generate"],
        [7, "Tiktok audio info  generate"],
        
    ]

    # Mencetak tabel menggunakan tabulate
    table = tabulate(data, headers=headers, tablefmt="fancy_grid")
    print(table)

    def get_user_choice():
        while True:
            user_input = input("Masukkan pilihan Anda (1/2/0) : ")
            if user_input in ['1', '2', '3']:
                return user_input
            else:
                print("Pilihan tidak valid. Silakan masukkan nomor pilihan yang benar.")
                
    def main():
        while True:
            TiktokTools()
            user_choice = get_user_choice()

            if user_choice == '1':
                print("menu belum tersedia")
        
            elif user_choice == '2':
                try:
                    subprocess.run(["python", "scraping1.py", ], check=True)
                except FileNotFoundError:
                    print("MAAF Ada kesalahan pastikan koneksi anda stabil")
            elif user_choice == "3":
                url=input("link video =>")
                download_youtube_video(url)

            elif user_choice == '0':
                print("Terima kasih telah menggunakan program ini.")
                break
TiktokTools()