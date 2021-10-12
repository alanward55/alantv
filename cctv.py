import os,time,re,sys,requests

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

os.system('clear')

print('Script ini dibuat oleh Alan Ward pada tanggal 9 april 2021 di negara Indonesia\n\n')
print('Pilih negara yang ingin kalin lihat cctv nya: ')
print (r+"[ 1 ]Indo",y+"nesia"),(r,w)
print (b+"[ 2 ]Italy"),(r,w)
print (cyan+"[ 3 ]Japan"),(r,w)
print (dgray+"[ 4 ]United States"),(r,w)
print (b+"[ 5 ]France"),(r,w)
print (cyan+"[ 6 ]Korea"),(r,w)
print (y+"[ 7 ]German"),(r,w)
print (g+"[ 8 ]Turkey"),(r,w)
print (r+"[ 9 ]Exit"),(r,w)
print ("\n")
pilih = input("\033[1;31m[ \033[1;37mPilih nomor\033[1;31m]\033[1;37m> ")    

if pilih == '1':
	import idn
elif pilih == '2':
	import it
elif pilih == '3':
	import jp
elif pilih == '4':
	import us
elif pilih == '5':
	import fr
elif pilih == '6':
	import kr
elif pilih == '7':
	import de
elif pilih == '8':
	import tr
elif pilih == '9':
	print('Copyright \N{COPYRIGHT SIGN} 2021 | Alan Ward')
	print (r+"Exiting ..."+w)
	time.sleep(3)
	os.sys.exit()
else:
	print('Maaf nomor yang anda masukkan tidak terdaftar, mohon dicoba kembali!')
	print('Copyright \N{COPYRIGHT SIGN} 2021 | Alan Ward')
	print (r+"Exiting ..."+w)
	time.sleep(2)
	os.sys.exit()
