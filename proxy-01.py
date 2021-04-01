import random
import requests
from colorama import Fore,Style
import threading
import time
print(Fore.GREEN+'''
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗      ██████╗  ██╗
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝     ██╔═████╗███║
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝█████╗██║██╔██║╚██║
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝ ╚════╝████╔╝██║ ██║
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║        ╚██████╔╝ ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝         ╚═════╝  ╚═╝

                   INSTA ---> @D_5TR
                   INSTA 01 ---> @ZER0ONE_01
                   MAKE BY ---> D5TR
                   TEAM ---> ZERO ONE  
''')

many = int(input('[*] Enter number proxy you went check up :'))

for ii2 in range(many):
    chois = random.randrange(400,9999)
    ##################################


    wax1 = random.choice( ['1', '2'] )
    chois2 = random.randrange(1,50)
    ################################

    wax2 = random.choice(['1', '2'])
    chois3 = random.randrange(1, 50)
    #################################
    wax3 = random.choice(['1', '2'])
    chois4 = random.randrange(1, 50)
    #################################
    wax4 = random.choice(['1', '2'])
    chois5 = random.randrange(1, 50)




    alls = str(wax1)+str(chois2)+'.'+str(wax2)+str(chois3)+'.'+str(wax3)+str(chois4)+'.'+str(wax4)+str(chois5)+':'+str(chois)

    with open('proxys.txt', 'a') as x:
        x.write(alls + '\n')
    print('[+] Done make proxy !','\n')

print('[*] wait to start chack proxy ...')
time.sleep(3)


r = requests.session()
proxy = open('proxys.txt', 'r').read().splitlines()

loghead = {
    'Host': 'www.instagram.com',
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64;rv: 87.0) Gecko / 20100101Firefox / 87.0',
    'Accept': '* / *',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'aSII4PZ8OZZ2XBqYlNNHNFK1Z1BphCVC',
    'X-Instagram-AJAX': '192f05fecd26',
    'X-IG-App-ID': '936619743392459',
    'X-IG-WWW-Claim': 'hmac.AR3Mzj_5DgFkWcc9xROX8fYAkhy32oHrg7mOXQyg5w9rBHs7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequestContent - Length: 274',
    'Origin': 'https//www.instagram.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/',
    'Cookie': 'ig_did=0DC19561-61BE-4A52-ADD1-03984BF455F6;mid=YBAnmQALAAHiYKh4a5RUSgw-ZvfH;ig_nrcb=1;shbid=5188;shbts=1617106294.4676127;rur=NAO;csrftoken=aSII4PZ8OZZ2XBqYlNNHNFK1Z1BphCVC',
    'TE': 'Trailers',

}


def chackproxy():
    while True:
        proxylist = []
        for pro in proxy:
            proxylist.append(pro)
            run = str(random.choice(proxylist))

        try:
            red = {
                'http': 'http://{}'.format(run),
                'https': 'https://{}'.format(run)

            }
            r.proxies = red
            url = 'https://www.instagram.com/accounts/login/ajax/'
            logdata = {
                "username": "d5tr",
                "enc_password": "#PWD_INSTAGRAM_BROWSER:10:1617281915:AWlQAJ21GW4F00dfy0iz65B+3w87lq0VbKAcWSK38AK/Hg14Vt46PRknmYCpn73XkhNZ3nnzKrAK4JiZ1n6aWVeEw8ZtOIbLjysr+xg8ak08toEiRqQclaXacD0E4pBwkCCym/P56dKNj8n4QNc=",

            }

            re = r.post(url, headers=loghead, data=logdata).text

            if ('"status":"ok"') in re:
                print(Fore.GREEN+'[+] GOOD PROXY --->', run)
                with open('proxy2.txt', 'a') as  good:
                    good.write(run + '\n')


            else:
                print(Fore.RED+'[-] BAD PROXY !!')


        except requests.exceptions.ConnectionError:
            print(Fore.RED+'[-] BAD PROXY !!')


thred = []

for i in range(many):
    thred1 = threading.Thread(target=chackproxy)
    thred1.start()
    thred.append(thred1)

for x1 in thred:
    x1.join()






