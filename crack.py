# coding: utf:8
#Import module
import platform
import time, os, sys, random
import urllib
import getpass
from getpass import *

home = os.getenv("HOME")
cokifile = home + "/.cookies"
garis = "-"*44


#color is warna
m = '\033[1;31m'  # merah (red)
h = '\033[1;32m'  # hijau (gren)
k = '\033[1;33m'  # kuning (yellow)
b = '\033[1;34m'  # biru (blue)
bb = '\033[34m'   # biru gelap (dark blue)
pi = '\033[1;35m' # ping (pink)
cyan = '\033[1;36m'  # biru muda (cyan)
z = '\033[0m'     # default / white


try:
    import requests
except ImportError:
    os.system("pip install requests")

url = "http://www.google.com"
timeout = 5
try:
    request = requests.get(url, timeout=timeout)
    print(f"{h}[+] OPEN THE PROGRAM ...{z}")
    time.sleep(1)
except (requests.ConnectionError, requests.Timeout) as exceptions:
    print(f"\n{m}[!] check your internet connection!{z}")
    sys.exit()


#logo tools
logo = f"""{b}

      ░██╗░░░░░░░██╗██╗███████╗██╗
      ░██║░░██╗░░██║██║██╔════╝██║
      ░╚██╗████╗██╔╝██║█████╗░░██║
      ░░████╔═████║░██║██╔══╝░░██║
      ░░╚██╔╝░╚██╔╝░██║██║░░░░░██║
      ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝

 ░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
 ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
 ██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░
 ██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░
 ╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗
 ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝{z}
               {k}𝕍𝕖𝕣𝕤𝕚𝕠𝕟 𝟙.𝟘{z}
 {cyan}           Powered by Franzz
 {h}          𝐏𝐞𝐦𝐚𝐥𝐚𝐧𝐠 𝐜𝐲𝐛𝐞𝐫 𝐭𝐞𝐚𝐦{z}
{b}{garis}{z}"""


def menu():
    os.system("clear")
    print(logo)
    print(f"""{b}[{h}𝟷{b}]{h} 𝚂𝚝𝚊𝚛𝚝 𝚙𝚛𝚘𝚐𝚛𝚊𝚖
{b}[{h}𝟸{b}]{h} 𝙸𝚗𝚜𝚝𝚊𝚕𝚕 𝚛𝚎𝚚𝚞𝚒𝚛𝚎d 𝚙𝚊𝚌𝚔𝚊𝚐𝚎
{b}[{h}𝟹{b}]{h} 𝚜𝚌𝚊𝚗 𝚗𝚎𝚊𝚛𝚋𝚢 𝚠𝚒𝚏𝚒
{b}[{h}𝟺{b}]{h} 𝚄𝚙𝚍𝚊𝚝𝚎 𝚙𝚛𝚘𝚐𝚛𝚊𝚖
{b}[{m}𝚡{b}]{m} 𝚎𝚡𝚒𝚝 𝙿𝚛𝚘𝚐𝚛𝚊𝚖""")
    mainmenu()
def mainmenu():
    while True:
        try:
            cmd=input(f"{b}[{k}?{b}]{k} 𝙲𝚑𝚘𝚘𝚜𝚎 𝚗𝚞𝚖𝚋𝚎𝚛: {h}")
            if int(len(cmd)) < 5:
                if cmd in ("x","X","exit"): exit(m+"[𝚎𝚡𝚒𝚝!]\n"+z)
                elif cmd in ("01","1"): mulai()
                elif cmd in ("02","2"): bahan()
                elif cmd in ("03","3"): scan()
                elif cmd in ("04","4"): update()
                else: continue
            else: continue
        except KeyboardInterrupt:
            exit(m+"\nAborted!"+z)

def bahan():
    os.system("clear")
    print(logo)
    print(f"{k}[{h}+{k}] downloading required package ... {h}")
    time.sleep(3)
    os.system('pip install --upgrade pip')
    os.system('apt install python -y')
    os.system('pip install tqdm')
    os.system('pip install alive_progress')
    os.system('apt install termux-api -y')
    os.system('pip install mechanize requests')
    from alive_progress import alive_bar
    for total in 5000, 7000, 4000, 0:
        with alive_bar(total) as bar:
            for _ in range(5000):
                time.sleep(.001)
                bar()
    print(f"{garis}\n{k}[{h}+{k}] installing file ...{z}")
    time.sleep(5)
    print(f"{h}[√] installing package successfully!\n{z}")
    getpass("[ PLEASE RESTART PROGRAM! ENTER TO CONTINUE ]")
    os.system("clear")
    print(logo)
    print(f"\n{h}[*] Usage: python or python3{z}\n")
    sys.exit()

def scan():
    os.system('clear')
    print(logo)
    print(f"{m}[!] please turn on your location!{z}")
    getpass("[ PRESS ENTER TO CONTINUE ]")
    print(f"{h}[{k}+{h}]{k} scanning wifi :{h}")
    time.sleep(2)
    animation = ["[■□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□]", "[■■■□□□□□□□□□□□□□□□□□]", "[■■■■□□□□□□□□□□□□□□□□]", "[■■■■■□□□□□□□□□□□□□□□]", "[■■■■■■□□□□□□□□□□□□□□]", "[■■■■■■■□□□□□□□□□□□□□]", "[■■■■■■■■□□□□□□□□□□□□]", "[■■■■■■■■■□□□□□□□□□□□]", "[■■■■■■■■■■□□□□□□□□□□]", "[■■■■■■■■■■■□□□□□□□□□]", "[■■■■■■■■■■■■□□□□□□□□]", "[■■■■■■■■■■■■■■□□□□□□]", "[■■■■■■■■■■■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print(f"\n{h}[√] done!{h}")
    time.sleep(1)
    os.system('clear')
    print(logo)
    os.system('termux-wifi-scaninfo')
    getpass(f"\n{z}[ PRESS ENTER TO QUIT ]")
    sys.exit()

def mulai():
    print(f"{h}[+] activate mobile wifi ....{z}")
    os.system("termux-wifi-enable true")
    print(f"{k}[+] turn on location ...{z}")
    os.system("termux-wifi-scaninfo")
    getpass(f"{m}[!] please turn on your location!{z}\n[ PRESS ENTER TO CONTINUE ]")
    os.system("clear")
    print(logo)
    os.system("termux-wifi-scaninfo")
    def main():
        while True:
            try:
                ndi=input(f"{h}[?] wifi target name: ")
                if ndi in (""): main()
                elif ndi in str(ndi):
                    def ndo():
                        while True:
                             ndx=input(f"{h}[?] bssid target number: ")
                             if ndi in ("", " "): ndo()
                             mul=input(f"{h}[?] start crack now [y/n] > ")
                             if mul in ("y","Y"):
                               print(f"{k}[*] cracking running ... please wait!{z}")
                               time.sleep(10)
                               print(f"{k}[*] handshaking using wordlist.txt")
                               time.sleep(5)
                               print(f"{m}[!] no [wordlist.txt] file found!{z}")
                               time.sleep(2)
                               print(f"{k}[+] using wordlist.txt default ... {z}")
                               time.sleep(1)
                               print(f"{h}[+] handshaking running ...{z}")
                               time.sleep(20)
                               print(f"{m}[×] correcting! wordlist.txt doesn't match{z}")
                               sys.exit()
                             elif mul in ("n","N"): menu()
                             else: continue
                    ndo()
                else: continue
            except KeyboardInterrupt:
                continue
    main()

def update():
    os.system("clear")
    print(logo)
    print(f"{h}[+] update program running ... {z}")
    time.sleep(7)
    print(f"{h}[√] update complete!{z}\n")
    getpass("[ PRESS ENTER TO EXIT ]")
    time.sleep(1)
    sys.exit()

menu()
mainmenu()
