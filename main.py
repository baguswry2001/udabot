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

def print_menu():
    header = "+------------------------------------+"
    print(header)
    print_colored("| No. |          Pilihan             |", Fore.WHITE, Back.BLUE)
    print(header)
    print_colored("|  1  | internet speed test          |", Fore.WHITE)
    print_colored("|  2  | google translate             |", Fore.WHITE)
    print_colored("|  3  | youtube video download       |", Fore.WHITE)
    print_colored("|  0  | youtube audio download       |", Fore.WHITE)
    print(header)
    



def get_user_choice():
    while True:
        user_input = input("Masukkan pilihan Anda (1/2/0) : ")
        if user_input in ['1', '2', '3']:
            return user_input
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor pilihan yang benar.")



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

        elif user_choice == '0':
            print("Terima kasih telah menggunakan program ini.")
            break


if __name__ == "__main__":
    main()



