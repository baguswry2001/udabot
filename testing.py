import requests
from colorama import Fore, Back, Style
from tabulate import tabulate
from urllib.parse import quote
def print_colored(text, color=Fore.WHITE, bg_color=Back.BLACK):
    print(bg_color + color + text + Style.RESET_ALL)
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
                return
            
            elif selected_idx == 8:
                return SpotifyTools()
            
            elif 0 <= selected_idx < len(datalist):
                download_song(datalist[selected_idx][-1], datalist[selected_idx][1])  # Menggunakan parameter unduhan
            else:
                print("Nomor lagu tidak valid.")
                
        elif selected_option == "x":
            print("Keluar dari SpotifyTools.")
            return
        else:
            print("Opsi tidak valid. Silakan pilih Y, D, atau X.")
SpotifyTools()
