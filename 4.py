import os, sys, re, requests, bs4, time, random, json, string
from bs4 import BeautifulSoup
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for
def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) !=1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session
ugen = []
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['5','6','7','8','9','10','11','12'])
    if b in ['5', '6', '7', '8', '9']:
        z=random.choice(['0', '1'])
        bv=b+'.'+z+'.'+z
    else:
        bv=b
    B=['GT-', 'SM-']
    c=random.choice(B)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    application_version = str(random.randint(111,396))+'.0.0.'+str(random.randrange(10,49))+'.'+str(random.randint(111,396))
    V=str(random.randrange(11,99))
    uas=f'{aa} {bv}; {c}{d}{e}{f} Build/{d}{f}{V}{f}; wv) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uas)
logo4 = """\33[1;32m

                 █████╗ ██╗  ██╗██╗     
                ██╔══██╗╚██╗██╔╝██║     
                ███████║ ╚███╔╝ ██║     
                ██╔══██║ ██╔██╗ ██║     
                ██║  ██║██╔╝ ██╗███████╗
                ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
\33[1;32m-------------------------------------------------------- 
  Owner      :  Alexander Grayson
  Facebook   :  AlexanderGraysonRecovery.IAmLimitless
  Tool Type  :  RPW Facebook Cloning Tool (Paid)
  Network    :  All Network
  Version    :  3.5
\33[1;32m--------------------------------------------------------"""
boy = ['Ethan Parker', 'Liam Anderson', 'Mason Taylor', 'Aiden Mitchell', 'Lucas Bennett', 'Oliver Cooper', 'Carter Walker', 'Jackson Brooks', 'Noah Scott', 'Avery Foster', 'William Hayes', 'James Turner', 'Michael Bryant', 'Benjamin Carter', 'Daniel Russell', 'Alexander Parker', 'Matthew Foster', 'Henry Mitchell', 'Samuel Harrison', 'David Brooks', 'Joseph Anderson', 'John Davis', 'Nicholas Wright', 'Andrew Reed', 'Jonathan Stewart', 'Christopher Kelly', 'Gabriel Price', 'Caleb Butler', 'Nathaniel Hughes', 'Anthony Morgan', 'Nicholas Sullivan', 'Christopher Powell', 'Sebastian Price', 'Zachary Murphy', 'Matthew Bennett', 'Dominic Hill', 'William Ward', 'Isaac King', 'Landon Harrison', 'Eli Foster', 'Logan Turner', 'Luke Hayes', 'Owen Mitchell', 'Wyatt Cooper', 'Henry Reid', 'Elijah Anderson', 'William Turner', 'Samuel Bryant', 'Oliver Russell', 'Ethan Parker', 'Liam Anderson', 'Mason Taylor', 'Aiden Mitchell', 'Lucas Bennett', 'Oliver Cooper', 'Carter Walker', 'Jackson Brooks', 'Noah Scott', 'Avery Foster', 'William Hayes', 'James Turner', 'Michael Bryant', 'Benjamin Carter', 'Daniel Russell', 'Alexander Parker', 'Matthew Foster', 'Henry Mitchell', 'Samuel Harrison', 'David Brooks', 'Joseph Anderson', 'John Davis', 'Nicholas Wright', 'Andrew Reed', 'Jonathan Stewart', 'Christopher Kelly', 'Gabriel Price', 'Caleb Butler', 'Nathaniel Hughes', 'Anthony Morgan', 'Nicholas Sullivan', 'Christopher Powell', 'Sebastian Price', 'Zachary Murphy', 'Matthew Bennett', 'Dominic Hill', 'William Ward', 'Isaac King', 'Landon Harrison', 'Eli Foster', 'Logan Turner', 'Luke Hayes', 'Owen Mitchell', 'Wyatt Cooper', 'Henry Reid', 'Elijah Anderson', 'William Turner', 'Samuel Bryant', 'Oliver Russell',
'Henry Porter', 'Maxwell Gray', 'Theodore Baker', 'Harrison Carter', 'Ezra Foster', 'Nolan Thompson', 'Lincoln Adams', 'Miles Evans', 'Nathaniel Hayes', 'Julian Sullivan', 'Oliver Foster', 'Benjamin Griffin', 'Alexander Fisher', 'Wyatt Richards', 'Oscar Turner', 'Hudson Wright', 'Sebastian Knight', 'Landon Parker', 'Caleb Brooks', 'Eli Stewart', 'Lucas Harrison', 'Mason Reynolds', 'Owen Powell', 'Daniel Morgan', 'James Bennett', 'Matthew Walker', 'Ethan Reed', 'Logan Turner', 'Aiden Murphy', 'Nathaniel Turner', 'William Griffin', 'Samuel Hayes', 'Elijah Foster', 'Christopher Bryant', 'Avery Price', 'David Mitchell', 'Gabriel Evans', 'Jackson Parker', 'Joseph Adams', 'Liam Bennett', 'Michael Richards']

girl = ['Aria Grace', 'Luna Violet', 'Aurora Jade', 'Scarlett Evangeline', 'Mila Rose', 'Stella Celeste', 'Amara Seraphina', 'Layla Skye', 'Vivienne Elise', 'Eleanor Ruby', 'Hazel Quinn', 'Aveline Ivy', 'Isla Belle', 'Nora Hazel', 'Willow Joy', 'Athena Pearl', 'Lila Maeve', 'Sophia Harper', 'Olivia Celestia', 'Isabella Claire', 'Ella Primrose', 'Grace Seraphina', 'Chloe Aurora', 'Lily Juliet', 'Ariana Eloise', 'Amelia Hope', 'Emily Florence', 'Scarlett Belle', 'Victoria Sage', 'Madeline Faye', 'Cora Everly', 'Harper Luna', 'Evelyn Aurora', 'Aria Willow', 'Luna Grace', 'Aurora Mae', 'Stella Violet', 'Vivienne Rose', 'Mila Jade', 'Layla Quinn', 'Scarlett Elise', 'Hazel Ruby', 'Aveline Seraphina', 'Isla Skye', 'Nora Celeste', 'Willow Seraphina', 'Athena Ivy', 'Lila Belle', 'Sophia Pearl', 'Olivia Maeve', 'Aria Grace', 'Luna Violet', 'Aurora Jade', 'Scarlett Evangeline', 'Mila Rose', 'Stella Celeste', 'Amara Seraphina', 'Layla Skye', 'Vivienne Elise', 'Eleanor Ruby', 'Hazel Quinn', 'Aveline Ivy', 'Isla Belle', 'Nora Hazel', 'Willow Joy', 'Athena Pearl', 'Lila Maeve', 'Sophia Harper', 'Olivia Celestia', 'Isabella Claire', 'Ella Primrose', 'Grace Seraphina', 'Chloe Aurora', 'Lily Juliet', 'Ariana Eloise', 'Amelia Hope', 'Emily Florence', 'Scarlett Belle', 'Victoria Sage', 'Madeline Faye', 'Cora Everly', 'Harper Luna', 'Evelyn Aurora', 'Aria Willow', 'Luna Grace', 'Aurora Mae', 'Stella Violet', 'Vivienne Rose', 'Mila Jade', 'Layla Quinn', 'Scarlett Elise', 'Hazel Ruby', 'Aveline Seraphina', 'Isla Skye', 'Nora Celeste', 'Willow Seraphina', 'Athena Ivy', 'Lila Belle', 'Sophia Pearl', 'Olivia Maeve',
'Penelope Grace', 'Hannah Violet', 'Sophie Camille', 'Leah Isolde', 'Evangeline Jane', 'Cecilia Mae', 'Avery Isabella', 'Natalia Everly', 'Ruby Seraphina', 'Violet Quinn', 'Zara Celestia', 'Athena Elise', 'Delilah Rose', 'Harlow Seraphina', 'Lucy Evangeline', 'Nina Belle', 'Astrid Juliet', 'Eloise Skye', 'Gemma Pearl', 'Maeve Harper', 'Juliet Ivy', 'Bianca Celeste', 'Seraphina Elara', 'Arabella Faye', 'Emery Willow', 'Elowen Maeve', 'Wren Seraphina', 'Mabel Celeste', 'Rosalie Mae', 'Serena Quinn', 'Cordelia Pearl', 'Elsie Aurora', 'Adeline Jade', 'Lila Seraphina', 'Fiona Grace', 'Tessa Celestia', 'Genevieve Ivy', 'Estelle Ruby', 'Harper Violet']
ok = []
cp = []
def menu():
    os.system('clear')
    print (logo4)
    print ('[1] New Account Generator')
    print (56*'-')
    sel = input('Select: ')
    if sel in['1', '01']:
        create().start()
    else:
        print ('select valid option')
        time.sleep(3)
        menu()
class create:

    def __init__(self):
        self.loop = 0
        self.gender = []

    def start(self):
        os.system('clear')
        print (logo4)
        print ('[1] BRP Accounts')
        print ('[2] GRP Accounts')
        print (56*'-')
        gen = input('Choose: ')
        print (56*'-')
        if gen in ['1', '01']:
            self.gender.append('boy')
        elif gen in ['2', '02']:
            self.gender.append('girl')
        else:
            self.gender.append('boy')
        print ('Example: 1000, 2000, 5000, 10000')
        print (56*'-')
        lim = int(input('Choose Quantity: '))
        os.system('clear')
        print (logo4)
        agent = random.choice(ugen)
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': '[FBAN/FB4A;FBAV/243.0.0.2.174;FBBV/156073738;FBDM/{density=3.0,width=1080,height=1493};FBLC/en_US;FBRV/324.0.0.9.130;FBCR/Tele2 Netherlands;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT2127-43;FBSV/10;FBOP/1;FBCA/arm64-v8a:]',
            'viewport-width': '980',
        }
        headers1 = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'upgrade-insecure-requests': '1',
            'user-agent': '[FBAN/FB4A;FBAV/243.0.0.2.174;FBBV/156073738;FBDM/{density=3.0,width=1080,height=1493};FBLC/en_US;FBRV/324.0.0.9.130;FBCR/Tele2 Netherlands;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT2127-43;FBSV/10;FBOP/1;FBCA/arm64-v8a:]',
        }
        print(' [•] Use airplane mode if no result. ')
        print (56*'-')
        OO = '\033[0;97m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r {OO}[ALEX-CREATING] {OO}{self.loop}/{str(lim)} | ALIVE: {len(ok)} | CHECKPOINT: {len(cp)}{OO} '),
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = random.choice(boy).split(' ')
                sex = '2'
            elif 'girl' in self.gender:
                name = random.choice(girl).split(' ')
                sex = '1'
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            passw = name[0]+name[1]+str(random.randint(111,999))
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1,28)),
                    "birthday_month": str(random.randint(1,12)),
                    "birthday_year": str(random.randint(1992,2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",
                })
                gett = self.ses.post('https://m.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id='+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                    print ('\r\033[1;33m [CHECKPOINT] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email+passw)
                                    print ('\r\033[1;33m [CHECKPOINT] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print ('\r\033[1;32m [ALEX-ALIVE] '+cok['c_user']+' | '+passw+' | '+coki+'\033[0;97m     ')
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
        print ('process has been completed')
        print (56*'-')
        print ('\033[1;32mTotal ids > ALIVE/' +str(len(ok)) + ' CHECKPOINT/' + str(len(cp)))
        print (56*'-')
        input('back')
        menu()
menu()
