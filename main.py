import subprocess
import platform


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
horizontal_line = Fore.RED + "==========================================" + Fore.RESET
print(Fore.GREEN+"+--------------------------------------+")
print(Fore.GREEN+"| WELCOME TO UDA BOT | LINUX CLI TOOLS |")
print(Fore.GREEN+"+--------------------------------------+")
print(Fore.GREEN+"+     jalankan ' udabot update ' untuk +")
print(Fore.GREEN+"+           memperbaruhi script        +")
print(Fore.GREEN+"+--------------------------------------+")

print(horizontal_line)
print(horizontal_line)

def print_menu():
    print("+------------------------------------+")
    print("| No. |          Pilihan             |")
    print("+------------------------------------+")
    print("|  1  | internet speed test          |")
    print("|  2  | google translate             |")
    print("|  0  | youtube viedo download       |")
    print("+------------------------------------+")



def get_user_choice():
    while True:
        user_input = input("Masukkan pilihan Anda (1/2/0) : ")
        if user_input in ['1', '2', '0']:
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


        elif user_choice == '0':
            print("Terima kasih telah menggunakan program ini.")
            break

if __name__ == "__main__":
    main()



