from colorama import Fore, Style, init
from anonfile import AnonFile
import os
import sys
from DoxLib import gsearch

# Colors + style implementation
br = Style.BRIGHT
seccolor = br + Fore.GREEN
primcolor = br + Fore.BLACK
white = br + Fore.WHITE

# Upload
anon = AnonFile()

# Functions
def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def logo():
    clear()
    print(f'''
	{primcolor} ██▓███ ▓██   ██▓▓█████▄  ▒█████  ▒██   ██▒
	▓██░  ██▒▒██  ██▒▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░
	▓██░ ██▓▒ ▒██ ██░░██   █▌▒██░  ██▒░░  █   ░
	▒██▄█▓▒ ▒ ░ ▐██▓░░▓█▄   ▌▒██   ██░ ░ █ █ ▒ 
	▒██▒ ░  ░ ░ ██▒▓░░▒████▓ ░ ████▓▒░▒██▒ ▒██▒
	▒▓▒░ ░  ░  ██▒▒▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
	░▒ ░     ▓██ ░▒░  ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░
	░░       ▒ ▒ ░░   ░ ░  ░ ░ ░ ░ ▒   ░    ░  
	         ░ ░        ░        ░ ░   ░    ░  
	         ░ ░      ░                        
	          			{white}Coded by: {seccolor} WtfIsThis
	          			{white}Version: {seccolor} 0.1''')

def goback():
	keyinput = input(f'''\n{primcolor}Write 'b' to go back to the menu and 'q' to exit the program\n{seccolor}[>] ''')
	if keyinput == 'b':
		main()
	elif keyinput == 'q':
		clear()
		sys.exit()
	else:
		clear()
		sys.exit('Invalid Input, ' + keyinput + " isn't defined" )

def Help():
	logo()
	print(f'''{primcolor}Help [-h] -\n\n{seccolor}''')
	goback()

def Github():
	logo()
	print(f'''{primcolor}Github -\n\n{seccolor}My Github profile: https://github.com/Wtf-Is-This-x1337''')
	print('Project repository: https://github.com/Wtf-Is-This-x1337/PyDox')
	print('[!] Code Improvements/Suggestions are welcome\n[!] Open an issue in Github for suggestions/issues')
	goback()

def Credits():
	logo()
	print(f'''{primcolor}Credits -\n\n{seccolor}[+] Creator - WtfIsThis\n-----------------------\nI stole code from:\n[+] Garuda - coder: Cryptonian007\n\tHis github: https://github.com/Cryptonian007\n[+] Sherlock project - coder: Siddharth Dushantha\n\tHis github: https://github.com/sdushantha\n[+] Anonfiles Unofficial Python API - coder: nstrydom2\n\tHis github: https://github.com/nstrydom2''')
	goback()

def Style():
	logo()
	styleoption = input(f'''{primcolor}Style -\n\n{seccolor}[1] Green | Bright Green (Default)\n[2] Cyan | Blue\n[3] Blue | Magenta\n\n[>] ''')
	goback()

def SetApi():
	logo()
	pastebinkey = input(f'''{primcolor}Set API Keys -\n\n{seccolor}[+] Pastebin API Key: ''')
	shodankey = input('[+] Shodan API Key: ')
	ipgeokey = input('[+] Ipgeolocation API Key: ')
	ApiFile = open("APIs.txt", "w")
	ApiFile.write(pastebinkey + "\n" + shodankey + "\n" + ipgeokey)
	ApiFile.close() # close the file when done
	print('Done! File created at ./APIs.txt')
	goback()

def AutoDox():
	logo()
	print(f'''{primcolor}Informations -\n\n{seccolor}''')
	goback()

def RealName():
    logo()
    print(f'''{primcolor}Dox using a real name -\n\n{seccolor}''')
    goback()

def Username():
    logo()
    print(f'''{primcolor}Dox using a username - \n\n{seccolor}''')
    goback()

def Phone():
    logo()
    print(f'''{primcolor}Dox using a username - \n\n{seccolor}''')
    goback()

def Address():
    logo()
    print(f'''{primcolor}Dox using an address - \n\n{seccolor}''')
    goback()

def Tools():
    logo()
    toolsinput = input(f'''{primcolor}Tools - \n\n{seccolor}[1] Sherlock\n[2] OSINT\n[3] ''')
    goback()

def CreateList():
    logo()
    print(f'''\n{primcolor}Create a list with all the informations - \n{seccolor}''')
    # ! "do u want to delete the last file created"
    listrealname = input('Real name: ')
    listusername = input('Username: ')
    listage = input('Age: ')
    listphone = input('Phone number: ')
    listcountry = input('Country: ')
    listcity = input('City: ')
    listaddress = input('Address: ')
    listip = input('IP address: ')
    listother = input('Other informations (separate by comma): ')
    # open list.txt for writing and create it if it doesn't exist 
    List = open("list.txt", "w") # or 'a+' for append mode
    List.write("List - \nReal name: " + listrealname + "\nUsername: " + listusername + "\nAge: " + listage + "\nPhone number: " + listphone + "\nCountry: " + listcountry + "\nCity: " + listcity + "\nAddress: " + listaddress + "\nIP Address: " + listip + "\nOther info - \n" + listother)
    List.close() # close the file when done
    print('Done! File created at ./list.txt')
    # upload
    print(f'''\n{primcolor}Do you want to upload the file online? [y/n]{seccolor}''')
    qupload = input('[>] ')
    if qupload == 'y':
    	option = input(f'''\n{primcolor}Choose an option:\n{seccolor}[1] Pastebin (next update | requires Api Key)\n[2] Anonfiles\n[3] More soon\n\n[>] ''')
    	if option == '2': # upload on anonfiles
    		# upload the file and enable progressbar terminal feedback
    		upload = anon.upload('./list.txt', progressbar=True)
    		print('List.txt was uploaded at: ' + upload.url.geturl())
    goback()

def main():
	logo()
	select = input(f'''{seccolor}\nSelect:
	1) {primcolor}Help\t\t{seccolor}2) {primcolor}Github\t  {seccolor}3) {primcolor}Credits\n
	{seccolor}4) {primcolor}Style\t{seccolor}5) {primcolor}Set API Keys\t  {seccolor}6) {primcolor}Auto Dox\n
    {seccolor}\t7) {primcolor}Real Name\t{seccolor}8) {primcolor}Username\t  {seccolor}9) {primcolor}Phone\n
    {seccolor}\t10) {primcolor}Address\t{seccolor}11) {primcolor}Tools\t {seccolor}12) {primcolor}Create List\n
                        {seccolor}13) {primcolor}Quit
	\n{seccolor}Option: ''')

	# full spaghetti
	if select == '1':
		Help()
	elif select == '2':
		Github()
	elif select == '3':
		Credits()
	elif select == '4':
		Style()
	elif select == '5':
		SetApi()
	elif select == '6':
		AutoDox()
	elif select == '7':
		RealName()
	elif select == '8':
		Username()
	elif select == '9':
		Phone()
	elif select == '10':
		Address()
	elif select == '11':
		Tools()
	elif select == '12':
		CreateList()
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
