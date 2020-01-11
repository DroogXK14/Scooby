# -*- coding: utf-8 -*-
# Coded By DemonSad and DroogXK (& Bot#3939)
# English : This script is in beta, we will release the second version soon.
# Portuguese : Este script esta em beta, lançaremos a segunda versão em breve.
# REQUIREMENTS: requests (pip install requests) & python 3
from requests import get
from sys import argv

api = {1: 'reverseiplookup', 2: 'whois', 3: 'httpheaders', 4: 'pagelinks', 5: 'dnslookup',
       7: 'subnetcalc', 8: 'geopip', 9: 'zonetransfer', 10: 'findshareddns', 11: 'mtr'}

def info(escolha):
    if escolha in [1,2,3,4,5,7,8,9,10,11]:
        print(get(f'https://api.hackertarget.com/{api[escolha]}/?q='+input('Target: ')).text)
    elif escolha == 6:
        with open('list.txt', 'r') as file:
            target = input('Target : ')
            print('\nScanning...\n')
            for line in file.readlines():
                if get(target + '/' + line.strip('\n')).status_code == 200:
                    print('Found : ' + line)
                    break

def sqliTest():
    errors_dbms = (r'SQL syntax.*MySQL', r'Warning.*mysql_.*', r'MySQL Query fail.*', r'SQL syntax.*MariaDB server',
        r'PostgreSQL.*ERROR', r'Warning.*\Wpg_.*', r'Warning.*PostgreSQL',
        r'OLE DB.* SQL Server', r'(\W|\A)SQL Server.*Driver', r'Warning.*odbc_.*', r'Warning.*mssql_',
        r'Msg \d, Level \d, State \d', r'Unclosed quotation mark after the character string',
        r'Microsoft OLE DB Provider for ODBC Drivers',r'Microsoft Access Driver',
        r'Access Database Engine', r'Microsoft JET Database Engine',r'.*Syntax error.*query expression',
        r'\bORA-[0-9][0-9][0-9][0-9]', r'Oracle error',r'Warning.*oci_.*','Microsoft OLE DB Provider for Oracle',
        r'CLI Driver.*DB2', r'DB2 SQL error', r'SQLite/JDBCDriver', r'System.Data.SQLite.SQLiteException',
        r'Warning.*ibase_.*', r'com.informix.jdbc',r'Warning.*sybase.*', r'Sybase message')

    resp = get(input('Target :  ') + '/%27')
    for err in errors_dbms:
        if err in resp.text:
            print('Vulnerability Found! : ' + err)
            exit()
    print('Vulnerability not found on ' + resp.url.strip('%27'))

if len(argv) == 1:
    print('Try using: python scooby.py <option number>\n')
    print('''01) Reverse IP Lookup\n02) Whois\n03) Http Header 
04) Extract Page Links\n05) DNS Lookup\n06) Admin Panel Finder
07) Subnet Lookup\n08) GEOIP Lookup\n09) Zone Transfer
10) Find Shared DNS\n11) Traceroute\n12) TCP Port Scan\n13) SQLi test
99) Exit\n''')
else:
    if argv[1] == '13': sqliTest()
    else: info(int(argv[1]))