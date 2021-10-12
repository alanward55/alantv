import os,re,sys,time, requests
b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
res = requests.get('https://www.insecam.org/en/bycountry/FR/', headers=headers)
findpage = re.findall('"?page=",\s\d+', res.text)[1]
rfindpage = findpage.replace('page=", ', '')
os.system('clear')

print("  \'========================================.  ")
print("  |Pemilik: Alan Ward    |Asli Indonesia   | ")
print("  |IG     : uli_karaba   |+62-853-2672-8933| ")
print("  \'========================================.  ")
print("  [Nomor cctv : 1, 2, 3, 4, 5, 6, 7, 8, 9,]")
page = input("\033[1;31m [ \033[1;37mPilih nomor cctv \033[1;31m]\033[1;37m> ")
animasi = ["Loading[□□□□□□□□□□]","Loading[■□□□□□□□□□]","Loading[■■□□□□□□□□]", "Loading[■■■□□□□□□□]", "Loading[■■■■□□□□□□]", "Loading[■■■■■□□□□□]", "Loading[■■■■■■□□□□]", "Loading[■■■■■■■□□□]", "Loading[■■■■■■■■□□]", "Loading[■■■■■■■■■□]", "Loading[■■■■■■■■■■]"]
for i in range(len(animasi)):
    time.sleep(0.3)
    sys.stdout.write("\r" + animasi[i % len(animasi)])
    sys.stdout.flush()
url = ("https://www.insecam.org/en/bycountry/FR/?page="+str(page))
print ("\n")
res = requests.get(url, headers=headers)
findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
count = 0
for _ in findip:
     hasil = (findip[count])
     print ('[ link ip cctv: ',hasil,']')
print('\nCopas salah satu link diataske browser\n\n\n')
print (g+"Terimakasih telah menggunakan script ini"+w)
print (g+'Copyright \N{COPYRIGHT SIGN} 2021 | Alan Ward')
