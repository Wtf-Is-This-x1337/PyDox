# library for PyDox.py
import shodan
import sys
import phonenumbers
import os
import requests
import random
import webbrowser as web
import pickle as pi
from phonenumbers import geocoder, carrier, timezone
from googlesearch import search
from colorama import Fore, Style, init
from time import sleep

# user agents from Garuda
user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7',
    'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
    'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)',
    'Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51',
    'Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
    'Opera/9.80 (Windows NT 5.1; U; MRA 5.5 (build 02842); ru) Presto/2.7.62 Version/11.00',
    'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00',
    'Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.7.39 Version/11.00'
]

def gsearch(query):
    # Objective: Performs a Google search [Top 15 results]
    lol = []
    results = search(query, tld='co.in', num=15, stop=15, pause=9)
    for i in results:
        lol.append(i)
    if len(lol) == 0:
        print(f'{b}{minus}{r} No results found{g}')
    else:
        for a in lol:
            print(f'{b}{plus}{cy} Retrieved URL: {g}{a}')
            sleep(1)
        file = 'googleresults.txt'
        with open(file, 'a') as f:
            f.write(f'[i] Query was: {query}\n')
            for j in lol:
                f.write(f'[+] URL: {j}\n')
            f.close()
        print(f'{b}{info}{g} Results saved to {w}{file}')

# Main
init()
# maybe later idk
