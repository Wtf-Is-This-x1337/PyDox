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
    clear()
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
	logo()
	print(f'''{ngreen}Help [-h] -\n\n{green}''')
	goback()

def github():
	logo()
	print(f'''{ngreen}Github -\n\n{green}My Github profile: https://github.com/Wtf-Is-This-x1337''')
	print('Project repository: https://github.com/Wtf-Is-This-x1337/PyDox')
	print('[!] Code Improvements/Suggestions are welcome\n[!] Open an issue in Github for suggestions/issues')
	goback()

def credits():
	logo()
	print(f'''{ngreen}Credits -\n\n{green}[+] Creator - WtfIsThis\n-----------------------\nI stole code from:\n[+] Garuda - coder: Cryptonian007\n\tHis github: https://github.com/Cryptonian007/\n[+] Sherlock project - coder: Siddharth Dushantha\n\tHis github: https://github.com/sdushantha''')
	goback()

def settings():
	logo()
	print(f'''{ngreen}Settings -\n\n{green}''')
	goback()

def SetApi():
	logo()
	print(f'''{ngreen}Set API Keys -\n\n{green}''')
	goback()

def AutoDox():
	logo()
	print(f'''{ngreen}Informations -\n\n{green}''')
	goback()

def RealName():
    logo()
    print(f'''{ngreen}Dox using a real name -\n\n{green}''')
    goback()

def username():
    logo()
    print(f'''{ngreen}Dox using a username - \n\n{green}''')
    goback()

def phone():
    logo()
    print(f'''{ngreen}Dox using a username - \n\n{green}''')
    goback()

def address():
    logo()
    print(f'''{ngreen}Dox using an address - \n\n{green}''')
    goback()

def tools():
    logo()
    print(f'''{ngreen}Tools - \n\n{green}''')
    goback()

def createList():
    logo()
    print(f'''\n{ngreen}Create a list with all the informations - \n{green}''')
    listrealname = input('Real name: ')
    listusername = input('Username: ')
    listphone = input('Phone number: ')
    listcountry = input('Country: ')
    listcity = input('City: ')
    listaddress = input('Address: ')
    listip = input('IP address: ')
    listother = input('Other informations (separate by comma): ')
    # open list.txt for writing and create it if it doesn't exist 
    List = open("list.txt", "a+")
    List.write("List - \nReal name: " + listrealname + "\nUsername: " + listusername + "\nPhone number: " + listphone + "\nCountry: " + listcountry + "\nCity: " + listcity + "\nAddress: " + listaddress + "\nIP Address" + listip + "\nOther info - \n" + listother)
    List.close # close the file when done
    print('Done! File created at ./list.txt')
    goback()

def main():
	logo()
	select = input(f'''{green}\nSelect:
	1) {ngreen}Help\t\t{green}2) {ngreen}Github\t  {green}3) {ngreen}Credits\n
	{green}4) {ngreen}Settings\t{green}5) {ngreen}Set API Keys\t  {green}6) {ngreen}Auto Dox\n
    {green}\t7) {ngreen}Real Name\t{green}8) {ngreen}Username\t  {green}9) {ngreen}Phone\n
    {green}\t10) {ngreen}Address\t{green}11) {ngreen}Tools\t {green}12) {ngreen}Create List\n
                        {green}13) {ngreen}Quit
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
	elif select == '7':
		RealName()
	elif select == '8':
		username()
	elif select == '9':
		phone()
	elif select == '10':
		address()
	elif select == '11':
		tools()
	elif select == '12':
		createList()
	elif select == '13':
		clear()
		sys.exit()
	else:
		clear()
		sys.exit('Invalid Input')

# Main
init()
clear()
main()
