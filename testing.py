import requests
from colorama import Fore, Back, Style
from tabulate import tabulate    
def print_colored(text, color=Fore.WHITE, bg_color=Back.BLACK):
    print(bg_color + color + text + Style.RESET_ALL)   
def SpotifyTools():
        print(Fore.GREEN , "                                   ›—›              ")
        print(Fore.GREEN , " —ííííí{›                     íí›  íí— ›íííz        ")
        print(Fore.GREEN , "›í{   ›{  —› ———›     ›———   —{í——›››››{í{———    ›—›")
        print(Fore.GREEN , "›íí{—››   ííí——{íí› {íí——{íí›—íí——›{í—›—íí——í{   íí›")
        print(Fore.GREEN , "  ›—{ííí—›íí    —í{—í{    —|| íí›  {í— ›íí  —í— íí› ")
        print(Fore.GREEN , " {    ›íí›íí›   {í—›íí    {í— íí›  {í— ›íí   {í—í{  ")
        print(Fore.GREEN , "›ííííííí› ííííííí{  ›íííííí›  {ííí—{í— ›íí   ›ííz   ")
        print(Fore.GREEN , "         ›í{                               ›{—íí    ")
        print(Fore.GREEN , "          ——                                ›—›     ")
        header = "+----------------------+"
        print(header)
        print_colored("|  Spotify Downloader  |", Fore.WHITE, Back.GREEN)
        print(header)
        judul_lagu =input("Masukan judul lagu => ")
        
        def Scrapspotify(url):
                response = requests.get(url)
                if response.status_code == 200:
                    return response.json()
                else:
                    print("Failed to fetch data from API")
                    return None
        url = f"https://aemt.me/search?query={judul_lagu}"
        data = Scrapspotify(url)
        api_data = data
        headers = ["NO", "Title", "Artist", "Duration", "Rate"]
        datalist = []
        for idx, track in enumerate(api_data["data"], start=1):
            row = [idx, track["title"], track["artist"], track["duration"], track["popularity"]]
            datalist.append(row)

        table = tabulate(datalist, headers=headers, tablefmt="fancy_grid")
        print(table)
        print("ya/no => lanjur cari/keluar")
        input("Masukan nomor untuk Mendownload")
        
        
SpotifyTools()