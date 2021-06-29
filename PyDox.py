from colorama import Fore, Style, init
import os
import sys

# Colors
br = Style.BRIGHT
green = br + Fore.GREEN
white = br + Fore.WHITE
ngreen = br + Fore.BLACK

# Functions
def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def logo():
	print(f'''
	{ngreen} ██▓███ ▓██   ██▓▓█████▄  ▒█████  ▒██   ██▒
	▓██░  ██▒▒██  ██▒▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░
	▓██░ ██▓▒ ▒██ ██░░██   █▌▒██░  ██▒░░  █   ░
	▒██▄█▓▒ ▒ ░ ▐██▓░░▓█▄   ▌▒██   ██░ ░ █ █ ▒ 
	▒██▒ ░  ░ ░ ██▒▓░░▒████▓ ░ ████▓▒░▒██▒ ▒██▒
	▒▓▒░ ░  ░  ██▒▒▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
	░▒ ░     ▓██ ░▒░  ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░
	░░       ▒ ▒ ░░   ░ ░  ░ ░ ░ ░ ▒   ░    ░  
	         ░ ░        ░        ░ ░   ░    ░  
	         ░ ░      ░                        
	          			{white}Coded by: {green} WtfIsThis
	          			{white}Version: {green} 0.1''')

def goback():
	keyinput = input(f'''\n{ngreen}Write 'b' to go back to the menu and 'q' to exit the program\n{green}[>] ''')
	if keyinput == 'b':
		main()
	elif keyinput == 'q':
		clear()
		sys.exit()
	else:
		clear()
		sys.exit('Invalid Input, ' + keyinput + " isn't defined" )

def help():
	clear()
	logo()
	print(f'''{ngreen}Help:\n{green}''')
	goback()

def github():
	clear()
	logo()
	print(f'''{ngreen}Github:\n{green}My Github profile: https://github.com/Wtf-Is-This-x1337''')
	print('Project repository: https://github.com/Wtf-Is-This-x1337/PyDox')
	print('!!\nCode Improvements/Suggestions are welcome\nOpen an issue in Github for suggestions/issues')
	goback()

def credits():
	clear()
	logo()
	print(f'''{ngreen}Credits:\n{green}[+] Creator - WtfIsThis\n-----------------------\nI stole code from:\n[+] Garuda - coder: Cryptonian007\n\tHis github: https://github.com/Cryptonian007/\n[+] Sherlock project - coder: Siddharth Dushantha\n\tHis github: https://github.com/sdushantha''')
	goback()

def settings():
	clear()
	logo()
	print(f'''{ngreen}Settings:\n{green}''')
	goback()

def SetApi():
	clear()
	logo()
	print(f'''{ngreen}Set API Keys:\n{green}''')
	goback()

def AutoDox():
	clear()
	logo()
	print(f'''{ngreen}Informations:\n{green}''')
	goback()

def main():
	clear()
	logo()
	select = input(f'''{green}\nSelect:
	1) {ngreen}Help\t\t{green}2) {ngreen}Github\t  {green}3) {ngreen}Credits\n
	{green}4) {ngreen}Settings\t{green}5) {ngreen}Set API keys\t  {green}6) {ngreen}Auto Dox
	\n{green}Option: ''')

	# full spaghetti
	if select == '1':
		help()
	elif select == '2':
		github()
	elif select == '3':
		credits()
	elif select == '4':
		settings()
	elif select == '5':
		SetApi()
	elif select == '6':
		AutoDox()
	else:
		clear()
		sys.exit('Invalid Input')

# Main
init()
clear()
main()
