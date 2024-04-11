import subprocess
import platform
from pytube import YouTube
from colorama import Fore, Back, Style

from pyfiglet import Figlet
from colorama import init, Fore
import sys
import time
from colorama import init, Fore
from tabulate import tabulate
from colorama import init, Fore
import subprocess
import os
init()
f = Figlet(font='slant')

ascii_art = f.renderText('- uda -')
table_data = [
    [Fore.GREEN + "create by:", "bagus wirayuda" + Fore.RESET]
]
table = tabulate(table_data, tablefmt="grid")
print(Fore.YELLOW + ascii_art + Fore.RESET )
horizontal_line = Fore.RED + "========================================" + Fore.RESET
print(Fore.GREEN+"+--------------------------------------+")
print(Fore.GREEN+"| WELCOME TO UDA BOT | LINUX CLI TOOLS |")
print(Fore.GREEN+"+--------------------------------------+")
print(Fore.GREEN+"+     jalankan ' udabot update ' untuk +")
print(Fore.GREEN+"+           memperbaruhi script        +")
print(Fore.GREEN+"+--------------------------------------+")

print(horizontal_line)
print(horizontal_line)


def download_youtube_video(url, output_path=None):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_title = yt.title
        file_size = video_stream.filesize
        print(Fore.GREEN + "Judul video:", video_title)
        print(Fore.GREEN + "Ukuran Video: {:.2f} MB".format(file_size / (1024 * 1024)))
        print(Fore.CYAN + "Sedang mendownload. Sabar ya...")
        if output_path:
            video_stream.download(output_path)
        else:
            video_stream.download()
        print(Fore.CYAN + "Download selesai.")
        print(Fore.RED + "                            // II \\\\")
        print(Fore.RED + "                           //  II  \\\\")
        print(Fore.RED + "                           \\\\  II  //")
        print(Fore.RED + "                            \\\\ <> //")
        print(Fore.RED + "      jika video tidak tidak tersedia di video mungkin anda ")
        print(Fore.RED + " perlu membukanya secara manual di folder udabot di perangkat anda <!>")
    except Exception as e:
        print(Fore.RED + "Gagal di-download. Periksa link atau jaringan cuy:", str(e))
        
    while True:
        rep = input("Ingin mendownload video lagi [YA/NO] => ").lower()
        if rep == "ya":
            url=input("link video => ")
            download_youtube_video(url)
            break
        elif rep == "no":
            main()
            break
        else:
            print(Fore.RED +"<!> MASUKAN PILIHAN YANG BENAR [ YA/NO ] <!>")
   
def download_audio_as_mp3(video_url):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(filename_prefix="audio_")
        print("Unduhan audio berhasil")
    except Exception as e:
        print("Gagal mengunduh audio:", str(e))
        
        
def print_colored(text, color=Fore.WHITE, bg_color=Back.BLACK):
    print(bg_color + color + text + Style.RESET_ALL)   


def TiktokTools():
    def ComentarGenerate():
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
        for _ in range(2):
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
                    
                if len(table_data) >= 40:
                    break
                    
            else:
                print("Gagal mendapatkan respons:", response.status_code)
                break
        print(tabulate(table_data[:40], headers=["Username", "komentar"], tablefmt="grid"))
    
    def TiktokDownloadVideo(): 
        import requests
        import re
        import uuid
        from bs4 import BeautifulSoup

        def extract_video_id(url):
            pattern = r'/video/(\d+)'
            match = re.search(pattern, url)
            if match:
                return match.group(1)
            else:
                return None 

        def download_video(url, filename):
            with open(filename, 'wb') as f:
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    f.write(response.content)
                    print("Video berhasil diunduh")
                else:
                    print("Gagal mengunduh video")

        url = input("Masukan Link video : ")
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        current_url = response.url
        IdVideo = extract_video_id(current_url)

        # Generate nama file acak menggunakan uuid
        random_filename = str(uuid.uuid4()) + ".mp4"

        url_video = f"https://www.tikwm.com/video/media/play/{IdVideo}.mp4"
        download_video(url_video, random_filename)
    
            
        
        
        
        
    
    def TiktokToolsmenu():
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
        headers = ["NO", "TOOLS",]
        data = [
            [1, "Tiktok download video"],
            [8, "Tiktok download all video frome profile"],
            [6, "Tiktok audio download"],
            [3, "Tiktok comment video generate"],
            [4, "Tiktok coment video generate + identity "],
            [5, "Tiktok user profile info generate"],
            [7, "Tiktok audio info  generate"],
        ]
        table = tabulate(data, headers=headers, tablefmt="fancy_grid")
        print(table)
    def get_user_choicetiktok():
        while True:
            user_input = input("Masukkan pilihan Anda (1/2/0) : ")
            if user_input in ['1', '2', '3']:
                return user_input
            else:
                print("Pilihan tidak valid. Silakan masukkan nomor pilihan yang benar.")
    def choicemenu():
        while True:
            TiktokToolsmenu()
            user_choice = get_user_choicetiktok()

            if user_choice == '1':
                TiktokDownloadVideo()
        
            elif user_choice == '2':
                try:
                    subprocess.run(["python", "scraping1.py", ], check=True)
                except FileNotFoundError:
                    print("MAAF Ada kesalahan pastikan koneksi anda stabil")
                    
            elif user_choice == "3":
                ComentarGenerate()

            elif user_choice == '0':
                print("Terima kasih telah menggunakan program ini.")
                break
    choicemenu()


def download_audio_as_mp3(video_url):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(filename_prefix="audio_")
        print("Unduhan audio berhasil")
    except Exception as e:
        print("Gagal mengunduh audio:", str(e))







def get_user_choice():
    while True:
        user_input = input("Masukkan pilihan Anda (1/2/0) : ")
        if user_input in ['1', '2', '3' ,'4', '5', '0']:
            return user_input
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor pilihan yang benar.")

def print_menu():
    header = "+------------------------------------+"
    print(header)
    print_colored("| No. |          Pilihan             |", Fore.WHITE, Back.BLUE)
    print(header)
    print_colored("|  1  | internet speed test          |", Fore.WHITE)
    print_colored("|  2  | google translate             |", Fore.WHITE)
    print_colored("|  3  | youtube video download       |", Fore.WHITE)
    print_colored("|  4  | youtube audio download       |", Fore.WHITE)
    print_colored("|  5  | TIKTOK Tools                 |", Fore.WHITE)
    print_colored("|  0  | logout                       |", Fore.WHITE)
    print(header)
    

def main():
    while True:
        print_menu()
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
        elif user_choice =="4":
            print("Anda memilih Audio Download (MP3).")
            download_audio_as_mp3
            
        elif user_choice == "5":
            TiktokTools()

        elif user_choice == '0':
            print("Terima kasih telah menggunakan program ini.")
            break


if __name__ == "__main__":
    main()



