# -*- coding: utf-8 -*
#!/usr/bin/python
#################################
import requests, re, urllib2, os, sys, codecs, random               
import requests_random_user_agent
requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time
import json                     
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
ktnred = '\033[31m'
ktngreen = '\033[32m'
ktn3yell = '\033[33m'
ktn4blue = '\033[34m'
ktn5purp = '\033[35m'
ktn6blueblue = '\033[36m'
ktn7grey = '\033[37m'
CEND = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")
#####################################
##########################################################################################
def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """      

        .__          __            _______ _________  
_______ |__|________|  | __ ___.__.\   _  \\______  \ 
\_  __ \|  |\___   /|  |/ /<   |  |/  /_\  \   /    / 
 |  | \/|  | /    / |    <  \___  |\  \_/   \ /    /  
 |__|   |__|/_____ \|__|_ \ / ____| \_____  //____/   
                  \/     \/ \/            \/          
                                                      

"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)



print_logo()
start_raw = raw_input("\n\033[91mGive,Me List Dear\033[97m:~# \033[97m")
crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
try:
    with open(start_raw, 'r') as f:
        ooo = f.read().splitlines()
except IOError:
	pass
	
try:
    ooo = list((ooo))
except NameError:
    print '\033[31mOpen Your Eyes!'
    sys.exit()
count=0
with open(start_raw,'r')as f:
 for line in f:
    count+=1
print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92mTOTAL WEBLIST=',count

##########################################################################################
def jamet1(url):
    try:
        #Agent1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        cek = requests.get(url+'/filemanager/dialog.php', verify=False, timeout=15)
        if '<input type="hidden" id="cur_dir" value="' in cek.text.encode('utf-8'):
            print(ktngreen + '[Ok] Wp' + '(' + url + ')' + CEND)
            open('single.txt', 'a').write(url+'/filemanager/dialog.php'+'\n')
        cek1 = requests.get(url+'/admin/filemanager/dialog.php', verify=False, timeout=15)
        if '<input type="hidden" id="cur_dir" value="' in cek1.text.encode('utf-8'):
            print(ktngreen + '[Ok] Wp' + '(' + url + ')' + CEND)
            open('single.txt', 'a').write(url+'/admin/filemanager/dialog.php'+'\n')
        cek2 = requests.get(url+'/assets/filemanager/dialog.php', verify=False, timeout=15)
        if '<input type="hidden" id="cur_dir" value="' in cek2.text.encode('utf-8'):
            print(ktngreen + '[Ok] Wp' + '(' + url + ')' + CEND)
            open('single.txt', 'a').write(url+'/assets/filemanager/dialog.php'+'\n')
        cek3 = requests.get(url+'/plugins/filemanager/dialog.php', verify=False, timeout=15)
        if '<input type="hidden" id="cur_dir" value="' in cek3.text.encode('utf-8'):
            print(ktngreen + '[Ok] Wp' + '(' + url + ')' + CEND)
            open('single.txt', 'a').write(url+'/plugins/filemanager/dialog.php'+'\n')
        cek4 = requests.get(url+'/admin/js/tinymce/plugins/filemanager/dialog.php', verify=False, timeout=15)
        if '<input type="hidden" id="cur_dir" value="' in cek4.text.encode('utf-8'):
            print(ktngreen + '[Ok] Wp' + '(' + url + ')' + CEND)
            open('single.txt', 'a').write(url+'/admin/js/tinymce/plugins/filemanager/dialog.php'+'\n')
        cek5 = requests.get(url+'/js/filemanager/dialog.php', verify=False, timeout=15)
        if '<input type="hidden" id="cur_dir" value="' in cek5.text.encode('utf-8'):
            print(ktngreen + '[Ok] Wp' + '(' + url + ')' + CEND)
            open('single.txt', 'a').write(url+'/js/filemanager/dialog.php'+'\n')
        cek6 = requests.get(url+'/assets/js/tinymce/plugins/filemanager/dialog.php', verify=False, timeout=15)
        if '<input type="hidden" id="cur_dir" value="' in cek6.text.encode('utf-8'):
            print(ktngreen + '[Ok] Wp' + '(' + url + ')' + CEND)
            open('single.txt', 'a').write(url+'/assets/js/tinymce/plugins/filemanager/dialog.php'+'\n')
        cek7 = requests.get(url+'/assets/admin/js/tinymce/plugins/filemanager/dialog.php', verify=False, timeout=15)
        if '<input type="hidden" id="cur_dir" value="' in cek7.text.encode('utf-8'):
            print(ktngreen + '[Ok] Wp' + '(' + url + ')' + CEND)
            open('single.txt', 'a').write(url+'/assets/admin/js/tinymce/plugins/filemanager/dialog.php'+'\n')
        cek8 = requests.get(url+'/js/tinymce/plugins/filemanager/dialog.php', verify=False, timeout=15)
        if '<input type="hidden" id="cur_dir" value="' in cek8.text.encode('utf-8'):
            print(ktngreen + '[Ok] Wp' + '(' + url + ')' + CEND)
            open('single.txt', 'a').write(url+'/js/tinymce/plugins/filemanager/dialog.php'+'\n')
        cek9 = requests.get(url+'/scripts/filemanager/dialog.php', verify=False, timeout=15)
        if '<input type="hidden" id="cur_dir" value="' in cek9.text.encode('utf-8'):
            print(ktngreen + '[Ok] Wp' + '(' + url + ')' + CEND)
            open('single.txt', 'a').write(url+'/scripts/filemanager/dialog.php'+'\n')
        cek10 = requests.get(url+'/js/tinymce/plugins/filemanager/dialog.php', verify=False, timeout=15)
        if '<input type="hidden" id="cur_dir" value="' in cek10.text.encode('utf-8'):
            print(ktngreen + '[Ok] Wp' + '(' + url + ')' + CEND)
            open('single.txt', 'a').write(url+'/js/tinymce/plugins/filemanager/dialog.php'+'\n')
        else:
            open('failed.txt', 'a').write(url+'\n')
            print(ktnred + '[Not]Wp' + '(' + url + ')' + CEND)
    except:
        pass
    pass
##########################################################################################
def Main():
    try:
        start = timer()
        pp = Pool(int(crownes))
        pp = pp.map(jamet1, ooo)
        print('TIME TAKE: ' + str(timer() - start) + ' S')
    except:
        pass


if __name__ == '__main__':
    Main()
    
