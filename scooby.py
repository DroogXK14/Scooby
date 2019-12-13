# -*- coding: utf-8 -*-
# Coded By DemonSad and DroogXK
# English : This script is in beta, we will release the second version soon.
# Portuguese : Este script está na versão beta, lançaremos a segunda versão em breve.

import os
import time

try:
    import requests
except:
    print 'Instale o Request : pip install request'
    exit()
try:
    from colorama import *
except:
    print 'Instale o Colorama : pip install colorama'
    exit()

os.system('clear||cls')


def banner():
    print(Fore.CYAN + Style.BRIGHT + '''

   _____                  __         
  / ___/_________  ____  / /_  __  __
  \__ \/ ___/ __ \/ __ \/ __ \/ / / /
 ___/ / /__/ /_/ / /_/ / /_/ / /_/ / 
/____/\___/\____/\____/_.___/\__, /  
                            /____/   
''' + Fore.RESET + Style.RESET_ALL)


def banner1():
    print(Fore.RED + Style.BRIGHT + ''' 
  -=========================================-
  | Author : DemonSad and DroogXK           |
  | Version : 1                             |
  | Contact : @Magnus_Security and @DroogXK |
  | Team : NewSec-Team                      |
  -=========================================-
''' + Fore.RESET + Style.RESET_ALL)


def banner4():
    print(Fore.CYAN + Style.BRIGHT + '''    
  -=========================================-
  | Author : DemonSad and DroogXK           |
  | Version : 1                             |
  | Contact : @Magnus_Security and @DroogXK |
  | Team : NewSec-Team                      |
  -=========================================-
''' + Fore.RESET + Style.RESET_ALL)


def web():
    print (Fore.GREEN + Style.BRIGHT + '''

[Web Application Attack]            

01) Sql Injection Test (Beta phase)
99) Exit 

            ''' + Fore.RESET + Style.RESET_ALL)


def banner2():
    print(Fore.RED + Style.BRIGHT + '''
                             ;\ 
                            |' \ 
         _                  ; : ; 
        / `-.              /: : | 
       |  ,-.`-.          ,': : | 
       \  :  `. `.       ,'-. : | 
        \ ;    ;  `-.__,'    `-.| 
         \ ;   ;  :::  ,::'`:.  `. 
          \ `-. :  `    :.    `.  \ 
           \   \    ,   ;   ,:    (\ 
            \   :., :.    ,'o)): ` `-. 
           ,/,' ;' ,::"'`.`---'   `.  `-._ 
         ,/  :  ; '"      `;'          ,--`. 
        ;/   :; ;             ,:'     (   ,:) 
          ,.,:.    ; ,:.,  ,-._ `.     \""'/ 
          '::'     `:'`  ,'(  \`._____.-'"' 
             ;,   ;  `.  `. `._`-.  \\ 
             ;:.  ;:       `-._`-.\  \`. 
              '`:. :        |' `. `\  ) \ 
                 ` ;:       |    `--\__,' 
                   '`      ,' 
                        ,-' 

''' + Fore.RESET + Style.RESET_ALL)


def panel():
    print(Fore.GREEN + Style.BRIGHT + '''

[Web Pentest / Information Gathering]

01) Reverse IP Lookup
02) Whois
03) Http Header 
04) Extract Page Links
05) DNS Lookup
06) Admin Panel Finder
07) Subnet Lookup
08) GEOIP Lookup
09) Zone Transfer
10) Find Shared DNS
11) Traceroute
12) TCP Port Scan
99) Exit     

''' + Fore.RESET + Style.RESET_ALL)


banner()
banner1()

print(Fore.GREEN + Style.BRIGHT + '''
01) Web Pentest / Information Gathering

02) Web Application Attack

99) Exit
''' + Fore.RESET + Style.RESET_ALL)


def one():
    try:
        escolha = raw_input(Fore.MAGENTA + Style.BRIGHT + 'Scooby> ' + Fore.RESET + Style.RESET_ALL)
        if escolha == '01' or escolha == '1':
            print(Fore.GREEN + Style.BRIGHT + '''

01) Reverse IP Lookup
02) Whois
03) Http Header 
04) Extract Page Links
05) DNS Lookup
06) Admin Panel Finder
07) Subnet Lookup
08) GEOIP Lookup
09) Zone Transfer
10) Find Shared DNS
11) Traceroute
12) TCP Port Scan
99) Exit
        ''' + Fore.RESET + Style.RESET_ALL)

        escolha2 = raw_input(Fore.MAGENTA + Style.BRIGHT + 'Scooby> ' + Fore.RESET + Style.RESET_ALL)
        if escolha2 == '1' or escolha2 == '01':
            os.system('clear||cls')
            banner2()
            banner4()
            col = raw_input(Fore.GREEN + Style.BRIGHT + 'Target  : ' + Fore.RESET + Style.RESET_ALL)
            api = 'https://api.hackertarget.com/reverseiplookup/?q='
            junto = (api + col)
            req = requests.get(junto)

            if "" in req.text:
                print (Fore.YELLOW + Style.BRIGHT + '[+] Loading...\n' + Fore.RESET + Style.RESET_ALL)
                time.sleep(3)
                print req.text
            else:
                if "error check your search parameter" in req.text:
                    print (Fore.RED + Style.BRIGHT + '[-] Error' + Fore.RESET + Style.RESET_ALL)

        if escolha2 == '2' or escolha2 == '02':
            os.system('clear||cls')
            banner2()
            banner4()
            col = raw_input(Fore.GREEN + Style.BRIGHT + 'Target  : ' + Fore.RESET + Style.RESET_ALL)
            api = 'https://api.hackertarget.com/whois/?q='
            junto = (api + col)
            req = requests.get(junto)

            if "" in req.text:
                print (Fore.YELLOW + Style.BRIGHT + '[+] Loading...\n' + Fore.RESET + Style.RESET_ALL)
                time.sleep(3)
                print req.text
            else:
                if "error check your search parameter" in req.text:
                    print (Fore.RED + Style.BRIGHT + '[-] Error' + Fore.RESET + Style.RESET_ALL)

        if escolha2 == '3' or escolha2 == '03':
            os.system('clear||cls')
            banner2()
            banner4()
            col = raw_input(Fore.GREEN + Style.BRIGHT + 'Target  : ' + Fore.RESET + Style.RESET_ALL)
            api = 'https://api.hackertarget.com/httpheaders/?q='
            junto = (api + col)
            req = requests.get(junto)

            if "" in req.text:
                print (Fore.YELLOW + Style.BRIGHT + '[+] Loading...\n' + Fore.RESET + Style.RESET_ALL)
                time.sleep(3)
                print req.text
            else:
                if "error check your search parameter" in req.text:
                    print (Fore.RED + Style.BRIGHT + '[-] Error' + Fore.RESET + Style.RESET_ALL)
        if escolha2 == '4' or escolha2 == '04':
            os.system('clear||cls')
            banner2()
            banner4()
            col = raw_input(Fore.GREEN + Style.BRIGHT + 'Target : ' + Fore.RESET + Style.RESET_ALL)
            api = 'https://api.hackertarget.com/pagelinks/?q='
            junto = (api + col)
            req = requests.get(junto)

            if "" in req.text:
                print (Fore.YELLOW + Style.BRIGHT + '[+] Loading...\n' + Fore.RESET + Style.RESET_ALL)
                time.sleep(3)
                print req.text
            else:
                if "error check your search parameter" in req.text:
                    print (Fore.RED + Style.BRIGHT + '[-] Error' + Fore.RESET + Style.RESET_ALL)

        if escolha2 == '5' or escolha2 == '05':
            os.system('clear||cls')
            banner2()
            banner4()
            col = raw_input(Fore.GREEN + Style.BRIGHT + 'Target : ' + Fore.RESET + Style.RESET_ALL)
            api = 'https://api.hackertarget.com/dnslookup/?q='
            junto = (api + col)
            req = requests.get(junto)

            if "" in req.text:
                print (Fore.YELLOW + Style.BRIGHT + '[+] Loading...\n' + Fore.RESET + Style.RESET_ALL)
                time.sleep(3)
                print req.text
            else:
                if "error check your search parameter" in req.text:
                    print (Fore.RED + Style.BRIGHT + '[-] Error' + Fore.RESET + Style.RESET_ALL)
        if escolha2 == '6' or escolha2 == '06':
            os.system('clear||cls')
            banner2()
            banner4()
            target = raw_input(Fore.GREEN + Style.BRIGHT + 'Target : ' + Fore.RESET + Style.RESET_ALL)
            with open('list.txt', 'r') as pwd:
                web = pwd.readlines()
                for trash in web:
                    x1 = (target + '/' + trash)
                    req = requests.get(x1)
                    if req.status_code == 200:
                        print(Fore.YELLOW + Style.BRIGHT + '\nScanning...\n' + Fore.RESET + Style.RESET_ALL)
                        print(Fore.GREEN + Style.BRIGHT + 'Found : ' + x1 + Fore.RESET + Style.RESET_ALL)
                        break
                    else:
                        pass

        if escolha2 == '7' or escolha2 == '07':
            os.system('clear||cls')
            banner2()
            banner4()
            col = raw_input(Fore.GREEN + Style.BRIGHT + 'Target  : ' + Fore.RESET + Style.RESET_ALL)
            api = 'https://api.hackertarget.com/subnetcalc/?q='
            junto = (api + col)
            req = requests.get(junto)

            if "" in req.text:
                print (Fore.YELLOW + Style.BRIGHT + '[+] Loading...\n' + Fore.RESET + Style.RESET_ALL)
                time.sleep(3)
                print req.text
            else:
                if "error check your search parameter" in req.text:
                    print (Fore.RED + Style.BRIGHT + '[-] Error' + Fore.RESET + Style.RESET_ALL)

        if escolha2 == '8' or escolha2 == '08':
            os.system('clear||cls')
            banner2()
            banner4()
            col = raw_input(Fore.GREEN + Style.BRIGHT + 'Target  : ' + Fore.RESET + Style.RESET_ALL)
            api = 'https://api.hackertarget.com/geoip/?q='
            junto = (api + col)
            req = requests.get(junto)

            if "" in req.text:
                print (Fore.YELLOW + Style.BRIGHT + '[+] Loading...\n' + Fore.RESET + Style.RESET_ALL)
                time.sleep(3)
                print req.text
            else:
                if "error check your search parameter" in req.text:
                    print (Fore.RED + Style.BRIGHT + '[-] Error' + Fore.RESET + Style.RESET_ALL)

        if escolha2 == '9' or escolha2 == '09':
            os.system('clear||cls')
            banner2()
            banner4()
            col = raw_input(Fore.GREEN + Style.BRIGHT + 'Target  : ' + Fore.RESET + Style.RESET_ALL)
            api = 'https://api.hackertarget.com/zonetransfer/?q='
            junto = (api + col)
            req = requests.get(junto)

            if "" in req.text:
                print (Fore.YELLOW + Style.BRIGHT + '[+] Loading...\n' + Fore.RESET + Style.RESET_ALL)
                time.sleep(3)
                print req.text
            else:
                if "error check your search parameter" in req.text:
                    print (Fore.RED + Style.BRIGHT + '[-] Error' + Fore.RESET + Style.RESET_ALL)

        if escolha2 == '10' or escolha2 == '10':
            os.system('clear||cls')
            banner2()
            banner4()
            col = raw_input(Fore.GREEN + Style.BRIGHT + 'Target  : ' + Fore.RESET + Style.RESET_ALL)
            api = 'https://api.hackertarget.com/findshareddns/?q='
            junto = (api + col)
            req = requests.get(junto)

            if "" in req.text:
                print (Fore.YELLOW + Style.BRIGHT + '[+] Loading...\n' + Fore.RESET + Style.RESET_ALL)
                time.sleep(3)
                print req.text
            else:
                if "error check your search parameter" in req.text:
                    print (Fore.RED + Style.BRIGHT + '[-] Error' + Fore.RESET + Style.RESET_ALL)

        if escolha2 == '11' or escolha2 == '11':
            os.system('clear||cls')
            banner2()
            banner4()
            col = raw_input(Fore.GREEN + Style.BRIGHT + 'Target  : ' + Fore.RESET + Style.RESET_ALL)
            api = 'https://api.hackertarget.com/mtr/?q='
            junto = (api + col)
            req = requests.get(junto)

            if "" in req.text:
                print (Fore.YELLOW + Style.BRIGHT + '[+] Loading...\n' + Fore.RESET + Style.RESET_ALL)
                time.sleep(3)
                print req.text
            else:
                if "error check your search parameter" in req.text:
                    print (Fore.RED + Style.BRIGHT + '[-] Error' + Fore.RESET + Style.RESET_ALL)

        if escolha2 == '99' or escolha2 == '99':
            os.system('clear||cls')
            banner2()
            banner4()
            exit()
    except (KeyboardInterrupt):
        print (Fore.RED + Style.BRIGHT + 'GoodBye' + Fore.RESET + Style.RESET_ALL)
    except:
        print (Fore.RED + Style.BRIGHT + 'GoodBye' + Fore.RESET + Style.RESET_ALL)


def two():
    try:
        errors_dbms = {
            'MySQL': (r'SQL syntax.*MySQL', r'Warning.*mysql_.*', r'MySQL Query fail.*', r'SQL syntax.*MariaDB server'),
            'PostgreSQL': (r'PostgreSQL.*ERROR', r'Warning.*\Wpg_.*', r'Warning.*PostgreSQL'),
            'Microsoft SQL Server': (
                r'OLE DB.* SQL Server', r'(\W|\A)SQL Server.*Driver', r'Warning.*odbc_.*', r'Warning.*mssql_',
                r'Msg \d+, Level \d+, State \d+', r'Unclosed quotation mark after the character string',
                r'Microsoft OLE DB Provider for ODBC Drivers'),
            'Microsoft Access': (
                r'Microsoft Access Driver', r'Access Database Engine', r'Microsoft JET Database Engine',
                r'.*Syntax error.*query expression'),
            'Oracle': (
                r'\bORA-[0-9][0-9][0-9][0-9]', r'Oracle error', r'Warning.*oci_.*',
                'Microsoft OLE DB Provider for Oracle'),
            'IBM DB2': (r'CLI Driver.*DB2', r'DB2 SQL error'),
            'SQLite': (r'SQLite/JDBCDriver', r'System.Data.SQLite.SQLiteException'),
            'Informix': (r'Warning.*ibase_.*', r'com.informix.jdbc'),
            'Sybase': (r'Warning.*sybase.*', r'Sybase message')
        }
        escolha = raw_input(Fore.MAGENTA + Style.BRIGHT + 'Scooby> ' + Fore.RESET + Style.RESET_ALL)
        if escolha == '02' or escolha == '2':
            os.system('clear||cls')
            banner2()
            banner4()
            web()
            escolha2 = raw_input(Fore.MAGENTA + Style.BRIGHT + 'Scooby> ' + Fore.RESET + Style.RESET_ALL)

            if escolha2 == '01' or escolha2 == '1':
                os.system('clear||cls')
                banner2()
                banner4()
                target = raw_input(Fore.GREEN + Style.BRIGHT + 'Target :  ' + Fore.RESET + Style.RESET_ALL)
                for dbms in errors_dbms:
                    x1 = (target + '%27')
                    req = requests.get(x1)
                    if dbms in req.text:
                        print (Fore.GREEN + Style.BRIGHT + 'Testing Payloads' + Fore.RESET + Style.RESET_ALL)
                        time.sleep(2)
                        print (Fore.GREEN + Style.BRIGHT + 'Vulnerable : ' + x1 + Fore.RESET + Style.RESET_ALL)
                        break
                    else:
                        print (Fore.RED + Style.BRIGHT + 'Not Vulnerable : ' + x1 + Fore.RESET + Style.RESET_ALL)
            if escolha2 == '99' or escolha2 == '99':
                exit()
                print (Fore.RED + Style.BRIGHT + 'GoodBye :)' + Fore.RESET + Style.RESET_ALL)

    except (KeyboardInterrupt):
        print (Fore.MAGENTA + Style.BRIGHT + 'GoodBye :(' + Fore.RESET + Style.RESET_ALL)
    except:
        print (Fore.MAGENTA + Style.BRIGHT + 'GoodBye :( ' + Fore.RESET + Style.RESET_ALL)


perguntax = raw_input(Fore.MAGENTA + Style.BRIGHT + 'Scooby> ' + Fore.RESET + Style.RESET_ALL)

if perguntax == '1' or perguntax == '01':
    os.system('clear||cls')
    banner2()
    print (Fore.MAGENTA + Style.BRIGHT + 'Enter 1 again for confirmation' + Fore.RESET + Style.RESET_ALL)
    one()
if perguntax == '02' or perguntax == '2':
    os.system('clear||cls')
    banner2()
    print (Fore.MAGENTA + Style.BRIGHT + 'Enter 2 again for confirmation' + Fore.RESET + Style.RESET_ALL)
    two()

if perguntax == '99' or perguntax == '99':
    print(Fore.MAGENTA + Style.BRIGHT + 'Goodbye ):' + Fore.RESET + Style.RESET_ALL)
    exit()