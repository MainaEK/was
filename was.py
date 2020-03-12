#!/usr/bin/env python3

import os
from urllib.parse import urlparse
from domain_enum.domain_enum import main

# Console Colors
G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'   # white

# Banner for the Tool
def banner():
    print ("""%s                                      
    __        ___    ____  
    \ \      / / \  / ___| 
     \ \ /\ / / _ \ \___ \ 
      \ V  V / ___ \ ___) |
       \_/\_/_/   \_\____/ 
                        %s%s
    """ % (G, W, Y))

# Creating Folders
def create_folder(dirName):
        if dirName.endswith('/'):
                dirName = dirName[:-1]

        if dirName.startswith('http://') or dirName.startswith('https://'):
                parse_object = urlparse(dirName)
                dirName = parse_object.netloc

        dir = 'WAS_scans/{}'.format(dirName)
        if not os.path.exists(dir):
                os.makedirs(dir)
                print(B + "[-] Directory", dir ,"created " + W)
        else:    
                print(B + "[-] Directory:" , dir ,"already exists " + W)
        return dir


def get_subdomains():
        domain = input('Enter the domain name: ')
        dir = create_folder(domain)
        output = main(domain,threads=30, savefile = dir+'/{}_subdomains.txt'.format(domain),ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)
        return output


def webapp_scan(url):
        dir = create_folder(url)
        if not url.startswith('http://') or not url.startswith('https://'):
                url = 'http://' + url

        if not url.endswith('/'):
                url = url + '/'

        domain = urlparse(url).netloc
        # os.system("echo {}".format(url))
        os.system("wapiti -u {} --color --flush-attack --flush-session -S aggressive -o {}".format(url,dir+'/{}_scan_report'.format(domain)))


def all():
        subdomains = get_subdomains()
        


def start():
    banner()
    ## Show menu ##
    print (30 * '-')
    print ("   M A I N - M E N U")
    print (30 * '-')
    print ("1. Domain Enumeration")
    print ("2. Web Application Scanning")
    print ("3. All")
    print (30 * '-')
    
    ## Get input ###
    choice = input('Enter your choice [1-3] : ')
    
    ### Convert string to int type ##
    choice = int(choice)
    
    ### Take action as per selected menu-option ###
    if choice == 1:
            get_subdomains()
    elif choice == 2:
            url = input('Enter the url name: ')
            webapp_scan(url)
    elif choice == 3:
            print ("Working progress")
        #     all()

    else:    ## default ##
            print ("Invalid number. Try again...")
            start()


start()


