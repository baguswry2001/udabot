# Hi, thank you for appreciating and using my program. If you are viewing this source code, it means you are an excellent developer. Please continue to provide your contributions and feedback through Telegram @baguswry101101
# hay terimakasih atas apresiasinya mengunakan program saya jika anda membukan source code ini itu artinya anda adalah seorang pengembang yang hebat terus berikan kamu kontribusi dan masukan lainya melalui telegram @baguswry101101

import subprocess
import requests
from pytube import YouTube
from colorama import Fore, Back, Style
from pyfiglet import Figlet
from colorama import init, Fore
from colorama import init, Fore
from tabulate import tabulate
from colorama import init, Fore
import subprocess
import re
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
        random_filename = str(uuid.uuid4()) + ".mp4"

        url_video = f"https://www.tikwm.com/video/media/play/{IdVideo}.mp4"
        download_video(url_video, random_filename)
        
    


    def TiktokDownloadAudio():
        import requests
        import re
        import uuid
        from bs4 import BeautifulSoup
        from moviepy.editor import VideoFileClip
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
                    print("generate link ")
                else:
                    print("Gagal mengenerate ")

        url = input("Masukan Link : ")
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        current_url = response.url
        IdVideo = extract_video_id(current_url)
        random_filename = str(uuid.uuid4()) + ".mp4"
        url_video = f"https://www.tikwm.com/video/media/play/{IdVideo}.mp4"
        download_video(url_video, random_filename)
        audio_filename = random_filename.split('.')[0] + ".mp3"
        video = VideoFileClip(random_filename)
        audio = video.audio
        audio.write_audiofile(audio_filename)
        video.close()
        import os
        os.remove(random_filename)
        return audio_filename

        
        
        
        
        
    
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
        headers = ["NO", "TIKTOK TOOLS",]
        data = [
            [1, "Download Video"],
            [2, "Download Audio "],
            [3, "Comment VIdeo Generate"],
            [4, "Audio info  generate"],
            [8, "Download all video frome profile"],
            [4, "coment video generate + identity "],
            [5, "user profile info generate"],
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
                TiktokDownloadAudio()
                print("Download audio berhasil....")
                
                    
            elif user_choice == "3":
                ComentarGenerate()

            elif user_choice == '0':
                print("Terima kasih telah menggunakan program ini.")
                break
    choicemenu()
# ===================================================== SPOTIFY TOOLS =================================================
def SpotifyToolss():
    from urllib.parse import quote
    def Scrapspotify(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data from API")
            return None
    def download_song(url, title):
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"{title}.mp3", 'wb') as file:
                file.write(response.content)
            print(f"Download '{title}.mp3' sukses!..")
        else:
            print(f"Gagal Mendownload: {response.status_code}")
    def SpotifyTools():
        print(Fore.GREEN, "                                   ›—›              ")
        print(Fore.GREEN, " —ííííí{›                     íí›  íí— ›íííz        ")
        print(Fore.GREEN, "›í{   ›{  —› ———›     ›———   —{í——›››››{í{———    ›—›")
        print(Fore.GREEN, "›íí{—››   ííí——{íí› {íí——{íí›—íí——›{í—›—íí——í{   íí›")
        print(Fore.GREEN, "  ›—{ííí—›íí    —í{—í{    —|| íí›  {í— ›íí  —í— íí› ")
        print(Fore.GREEN, " {    ›íí›íí›   {í—›íí    {í— íí›  {í— ›íí   {í—í{  ")
        print(Fore.GREEN, "›ííííííí› ííííííí{  ›íííííí›  {ííí—{í— ›íí   ›ííz   ")
        print(Fore.GREEN, "         ›í{                               ›{—íí    ")
        print(Fore.GREEN, "          ——                                ›—›     ")
        header = "+----------------------+"
        print(header)
        print_colored("|  Spotify Downloader  |", Fore.WHITE, Back.GREEN)
        print(header)
        judul_lagu = input("Masukan judul lagu => ")
        url = f"https://aemt.me/search?query={judul_lagu}"
        data = Scrapspotify(url)
        if not data or "data" not in data:
            print("Tidak ada data lagu yang ditemukan.")
            return
        headers = ["NO", "Title", "Artist", "Duration", "Rate"]
        datalist = []
        for idx, track in enumerate(data["data"], start=1):
            row = [idx, track["title"], track["artist"], track["duration"], track["popularity"]]
            link = track["url"]
            encoded_url = quote(link)
            parameter = f"https://aemt.me/download?url={encoded_url}"
            row.append(parameter)
            datalist.append(row)
        columns_to_print = [0, 1, 2, 3, 4] 
        datalist_to_print = [[row[i] for i in columns_to_print] for row in datalist]
        print(tabulate(datalist_to_print, headers=headers, tablefmt="fancy_grid"))
        while True:
            selected_option = input("Masukkan opsi untuk dilakukan (Y: Cari lagi, D: Download, X: Keluar) => ").strip().lower()
            if selected_option == "y":
                return SpotifyTools()
            
            elif selected_option == "d":
                selected_idx = int(input("Masukkan nomor untuk Mendownload (0 keluar, 9 cari lagi) => ")) - 1
                if selected_idx == -1:
                    return main()
                
                elif selected_idx == 8:
                    return SpotifyTools()
                
                elif 0 <= selected_idx < len(datalist):
                    download_song(datalist[selected_idx][-1], datalist[selected_idx][1])  # Menggunakan parameter unduhan
                else:
                    print("Nomor lagu tidak valid.")
                    
            elif selected_option == "x":
                print("Keluar dari SpotifyTools.")
                return main()
            else:
                print("Opsi tidak valid. Silakan pilih Y, D, atau X.")
    SpotifyTools()
# ===================================================== SPOTIFY TOOLS =================================================
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
        if user_input in ['1', '2', '3' ,'4', '5', '6','7','0']:
            return user_input
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor pilihan yang benar.")
def print_menu():
    header = "+------------------------------------+"
    print(header)
    print_colored("| No. |          Pilihan             |", Fore.WHITE, Back.BLUE)
    print(header)
    print_colored("|  1  | Internet speed test          |", Fore.WHITE)
    print_colored("|  2  | Google translate             |", Fore.WHITE)
    print_colored("|  3  | Youtube video download       |", Fore.WHITE)
    print_colored("|  4  | Youtube audio download       |", Fore.WHITE)
    print_colored("|  5  | Tiktok Tools                 |", Fore.WHITE)
    print_colored("|  6  | Spotify search & download    |", Fore.WHITE)
    print_colored("|  7  | Capcut video & audio Download|", Fore.WHITE)
    print_colored("|  8  | LK21 No Ads & Download       |", Fore.WHITE)
    print_colored("|  9  | CINEMA INDO No Ads & Download|", Fore.WHITE)
    print_colored("|  0  | logout                       |", Fore.WHITE)
    print(header)
# ===================================================== CAPCUT TOOLS =================================================
def capcut_tools():
    def viu():
        print(' ██████╗ █████╗ ██████╗  ██████╗██╗   ██╗████████╗')
        print('██╔════╝██╔══██╗██╔══██╗██╔════╝██║   ██║╚══██╔══╝')
        print('██║     ███████║██████╔╝██║     ██║   ██║   ██║   ')
        print('██║     ██╔══██║██╔═══╝ ██║     ██║   ██║   ██║   ')
        print('╚██████╗██║  ██║██║     ╚██████╗╚██████╔╝   ██║   ')
        print('╚═════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═════╝    ╚═╝   ')
    def cmenu():
        print(Fore.YELLOW+"+----------------------------------------+")
        print(Fore.YELLOW+"| CAPCUT TEMPLATE VIDEO & AUDIO DOWNLOAD |")
        print(Fore.YELLOW+"+----------------------------------------+")
        print(Fore.YELLOW+"| 1. CAPCUPT TEMPLATE VIDEO DOWNLOAD     |")
        print(Fore.YELLOW+"| 2. CAPCUT TEMPLATE AUDIO DOWNLOAD      |")
        print(Fore.YELLOW+"+----------------------------------------+")
    def c_get_user_choice():
        while True:
            user_input = input("Masukkan pilihan Anda (1/2/0) : ")
            if user_input in ['1', '2','0']:
                return user_input
            else:
                print("Pilihan tidak valid. Silakan masukkan nomor pilihan yang benar.")
    
    def url_input():
        pattern_long = re.compile(r'^https://www\.capcut\.com/templates/(\d+).*')
        pattern_short = re.compile(r'^https://www\.capcut\.com/t/([A-Za-z0-9]+).*')
        
        url = input("Masukkan URL CapCut: ")
        
        match_long = pattern_long.match(url)
        match_short = pattern_short.match(url)
        
        if match_long:
            template_id = match_long.group(1)
            print(f'ID Template: {template_id}')
            return template_id
        elif match_short:
            return get_capcut_download_url(capcut_url=url)
        else:
            print("URL tidak valid")
            return None

    def get_capcut_download_url(capcut_url):
        api_url = 'https://ssscap.net/api/download/get-url'
        params = {'url': capcut_url}
        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()
            data = response.json()
            template_id = re.search(r'(\d+)', data.get('url')).group(1)
            return template_id
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except requests.exceptions.RequestException as req_err:
            print(f'Request error occurred: {req_err}')
        except ValueError:
            print('Error decoding JSON response')
        return None

    def generate_video():
        link = url_input()
        if not link:
            print("ID template tidak ditemukan. Tidak dapat melanjutkan.")
            return
        
        url = f"https://ssscap.net/api/download/{link}"
        headers = {
            "Cookie": "__gads=ID=ba759bc380c8540c:T=1718204375:RT=1718204375:S=ALNI_MYW0-VR8k-LbsN317BxaXyurgAxxg; __gpi=UID=00000e48d499ad2a:T=1718204375:RT=1718204375:S=ALNI_MYkm_84bl57fa9e_TS-UbfS6wasTA; __eoi=ID=6d523f5f3499347f:T=1718204375:RT=1718204375:S=AA-AfjYEUmgeyqXdktlJcIGjYR2m; sign=38103ebfc9fe7380ca2510393a438025; device-time=1718204484726; FCNEC=%5B%5B%22AKsRol-9_C1d7rcyfb4a3CskWwZAammHf8ON6IdAiuKZlvxQonFgj9pLkpQQXZ7FnN-K5DWNzapQjXJcNPHzTPS7KSpkLdK1Zf-BBi519IxhNMV4wKtsZ0z9farqQeOlnPM0HRiVKd7naAAGrrn-vdwrr3rB39u-PQ%3D%3D%22%5D%2Cnull%2C%5B%5B2%2C%22%5Bnull%2C%5Bnull%2C3%2C%5B1718204377%2C686314000%5D%5D%5D%22%5D%5D%5D",
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response_json = response.json()
            original_video_url = response_json["originalVideoUrl"]
            name = response_json['title']
            video_url = f'https://ssscap.net{original_video_url}'
            
            video_response = requests.get(video_url)
            video_response.raise_for_status()
            
            with open(f"{name}.mp4", "wb") as f:
                f.write(video_response.content)
            print("Video berhasil didownload!")
            
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except requests.exceptions.RequestException as req_err:
            print(f'Request error occurred: {req_err}')
        except Exception as e:
            print("Terjadi kesalahan saat melakukan permintaan ke API:", e)

    
    def main_capcut():
        while True:
            viu()
            cmenu()
            user_choice = c_get_user_choice()
            if user_choice == '1':
                generate_video()
            elif user_choice == "2":
                SpotifyToolss()
            elif user_choice == '0':
                print("Terima kasih telah menggunakan program ini.")
                break
            else:
                print("Pilihan tidak valid, silakan coba lagi.")
    main_capcut()
# ===================================================== CAPCUT TOOLS =================================================
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
            
        elif user_choice == "6":
            SpotifyToolss()
        elif user_choice == "7":
            capcut_tools()
            
        elif user_choice == '0':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
if __name__ == "__main__":
    main()



