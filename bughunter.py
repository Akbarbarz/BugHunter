#!/usr/bin/env python2.7 
# __________                 ___ ___               __
# \______   \__ __  ____    /   |   \ __ __  _____/  |_  Mood By Akbarbarz
#  |    |  _/  |  \/ ___\  /    ~    \  |  \/    \   __\/ __ \_  __ \
#  |    |   \  |  / /_/  > \    Y    /  |  /   |  \  | \  ___/|  | \/
#  |______  /____/\___  /   \___|_  /|____/|___|  /__|  \___  >__|
#         \/     /_____/          \/            \/          \/
#

import os
import time
import httplib
import subprocess
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading
#import requests
import base64
from getpass import getpass
from commands import *
from sys import argv
from platform import system
from urlparse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep

os.system('clear')
os.system('clear')
os.system('mkdir ~/bughunter')
os.system('mkdir ~/bughunter/info')
os.system('mkdir ~/bughunter/mapp')
os.system('mkdir ~/bughunter/disc')
os.system('mkdir ~/bughunter/expt')
os.system('mkdir ~/bughunter/repo')
os.system('mkdir ~/bughunter/sage')
os.system("rm ~/bughunter/update.sh")
os.system('clear')
os.system('clear')

yes = set(['yes', 'y', 'Yes', 'Y'])
no = set(['no', 'n', 'No', 'N'])

###############################################################################

def logo():
    print """
- Mood by Venom Reyy 
"""
bughunterlogo = """\033[0m
  __________                 ___ ___               __                 
  \______   \__ __  ____    /   |   \ __ __  _____/  |Mood by Akbarbarz
   |    |  _/  |  \/ ___\  /    ~    \  |  \/    \   __\/ __ \_  __ \ 
   |    |   \  |  / /_/  > \    Y    /  |  /   |  \  | \  ___/|  | \/ 
   |______  /____/\___  /   \___|_  /|____/|___|  /__|  \___  >__|    
          \/     /_____/          \/            \/          \/        
\033[91m"""

# MENU ########################################################################

def menu():
    clearScr()
    print (bughunterlogo + """\033[1m
  [!] Alat Teratas untuk Berburu Bug [!] | Mood Bahasa Indonesia
 ---------------------------------------------------------------------
\033[0m
   [1] - Pengumpulan Informasi
   [2] - Pemetaan
   [3] - Penemuan
   [4] - Eksploitasi
   [5] - P0C & Pelaporan
   [6] - Perbarui BugHunter
   [7] - Tentang BugHunter
   [8] - IP dan Lokasi Anda
   [9] - New Tools By Venom Reyy
   [10] - Keluar dari BugHunter
 """)
    choice = raw_input("   Reyy Project~# ")
    os.system('clear')
    if choice == "6":
        updatebughunter()
    elif choice == "1":
        info()
    elif choice == "2":
        mapping()
    elif choice == "3":
        discovery()
    elif choice == "4":
        exploit()
    elif choice == "5":
        reporting()
    elif choice == "7":
        about()
    elif choice == "8":
        myinfo()
    elif choice == "9":
        sage()
    elif choice == "10":
        clearScr(), sys.exit()
    elif choice == "":
        clearScr(), menu()
    else:
        clearScr(), menu()

# Pengumpulan Informasi #######################################################

def info():
    clearScr()
    print(bughunterlogo)
    print("""
    Pengumpulan Informasi | Mood Bahasa Indonesia
    ----------------------------------------------------------------
    
     [0] - Tautan Berguna
     [1] - Perintah Dasar
     [2] - Masscan
     [3] - Pengintaian DNS
     [4] - Sublist3r
     [5] - Alt-DNS
     [6] - Mengumpulkan
     [7] - Subpenemu
     [8] - enumall
     [9] - Aquatone
    [10] - Cloudflare_Enum
    [11] - InfoG
    [12] - Pemanen
    [13] - Recon-NG
    [14] - SetoolKit
    [15] - WhatWeb
    [16] - Maltego
    [17] - Goohak
    [18] - GoogD0rker
    """)
    print("   [99] - Kembali ke Menu Utama \n")
    choice1 = raw_input("   Reyy Project~# ")
    if choice1 == "1":
        clearScr()
        basiccmd()
    if choice1 == "2":
        clearScr()
        masscan()
    if choice1 == "3":
        clearScr()        
        dnsrecon()
    if choice1 == "4":
        clearScr()
        sublister()
    if choice1 == "5":
        clearScr()
        altdns()
    if choice1 == "6":
        clearScr()
        amass()
    if choice1 == "7":
        clearScr()
        subfinder()
    if choice1 == "8":
        clearScr()
        enumall()
    if choice1 == "9":
        clearScr()
        aquatone()
    if choice1 == "10":
        clearScr()
        cloudenum()
    if choice1 == "11":
        clearScr()
        infog()
    if choice1 == "12":
        clearScr()
        harvester()
    if choice1 == "13":
        clearScr()
        reconng()
    if choice1 == "14":
        clearScr()
        setoolkit()
    if choice1 == "15":
        clearScr()
        whatweb()
    if choice1 == "16":
        clearScr()
        maltego()
    if choice1 == "17":
        clearScr()
        goohak()
    if choice1 == "18":
        clearScr()
        googdorker()
    if choice1 == "0":
        clearScr()
        usefullinks()                
    elif choice1 == "99":
        clearScr()
        menu()
    elif choice1 == "":
        clearScr()
        info()
    else:
        clearScr()
        info()

# Pemetaan #####################################################################

def mapping():
    clearScr()
    print(bughunterlogo)
    print("""
    Pemetaan | Mood Bahasa Indonesia
    ----------------------------------------------------------------
    
    [1] - Nmap
    [2] - Firefox
    [3] - Ekstensi Firefox
    [4] - Burp Suite Pro
    [5] - Ekstensi Burp Suite
    [6] - Muatan Penyusup
    [7] - Memuat Semua Hal
    [8] - Git-semua-Rahasia
    """)
    print("   [99] - Kembali ke Menu Utama \n")
    choice2 = raw_input("   Reyy Project~# ")
    if choice2 == "1":
        clearScr()
        nmap()
    elif choice2 == "2":
        clearScr()
        firefox()
    elif choice2 == "3":
        clearScr()
        firefoxext()
    elif choice2 == "4":
        clearScr()
        burpsuitepro()        
    elif choice2 == "5":
        clearScr()
        burpext()
    elif choice2 == "6":
        clearScr()
        intruderpayload()
    elif choice2 == "7":
        clearScr()
        allpayload()
    elif choice2 == "8":
        clearScr()
        gitallsec()    
    elif choice2 == "99":
        clearScr()
        menu()    
    elif choice2 == "":
        clearScr()
        mapping()    
    else:
        clearScr()
        mapping()

# Penemuan ###################################################################

def discovery():
    clearScr()
    print(bughunterlogo)
    print("""
    Penemuan | Mood Bahasa Indonesia
    ----------------------------------------------------------------
    
     [1] - Acunetix-WVS           [11] - W3af
     [2] - Arachni                [12] - Zed Attack Proxy
     [3] - Burp Suite             [13] - WP-Scan
     [4] - Nexpose                [14] - FuzzDB
     [5] - Nikto                  [15] - CeWL
     [6] - Vega                   [16] - DirBuster
     [7] - Wapiti                 [17] - Dirb
     [8] - Web Security Scanner   [18] - Filebuster
     [9] - Websecurify Suite      [19] - Gobuster
    [10] - Joomscan               [20] - DirSearch
    """)
    print("   [99] - Kembali ke Menu Utama \n")
    choice3 = raw_input("   Reyy Project~# ")
    os.system('clear')
    if choice3 == "1":
        acunetix()
    if choice3 == "2":
        arachni()
    if choice3 == "3":
        burpsuite()        
    if choice3 == "4":
        nexpose()
    if choice3 == "5":
        nikto()
    if choice3 == "6":
        vega()
    if choice3 == "7":
        wapiti()
    if choice3 == "8":
        websecscan()
    if choice3 == "9":
        websecsuite()
    if choice3 == "10":
        joomscan()
    if choice3 == "11":
        waaaf()
    if choice3 == "12":
        zed()
    if choice3 == "13":
        wpscan()        
    if choice3 == "14":
        fuzzdb()
    if choice3 == "15":
        cewl()
    if choice3 == "16":
        dirbuster()
    if choice3 == "17":
        dirb()
    if choice3 == "18":
        filebuster()
    if choice3 == "19":
        gobuster()
    if choice3 == "20":
        dirsearch()    
    elif choice3 == "99":
        menu()
    elif choice3 == "":
        clearScr()
        discovery()    
    else:
        clearScr()
        discovery()    

# Exploitation ###############################################################

def exploit():
    clearScr()
    print(bughunterlogo)
    print("""
    Eksploitasi | Mood Bahasa Indonesia
-----------------------------------------------------------------
    Mood Menu By Akbarbarz
-----------------------------------------------------------------
    [1] XSS Radar 
    [2] XSSHunter
    [3] xssHunterClient
    [4] DOMxssScanner
    [5] XSSer
    [6] BruteXSS
    [7] XSStrike
    [8] XSS'OR
    [9] SQLmap
   [10] OXML-xxe 
   [11] XXEinjextor
   [12] Tplmap
   [13] SSRF-Detector 
   [14] Ground Control  
   [15] LFISuit
   [16] Gen-xbin-Avi 
   [17] GitTools
   [18] DVCS Ripper
   [19] TKO Subs 
   [20] SubBruteforcer
   [21] Second-Order 
   [22] Race The Web
   [23] CORStest
   [24] RCE Struts-pwn
   [25] ysoSerial
   [26] PHPGGC
   [27] Ground Control 
   [28] Getsploit
   [29] Findsploit
   [30] BFAC
   [31] WP-Scan 
   [33] CMSmap
   [33] Joomscan
   [34] JSON W T T 
   [35] Wfuzz
   [36] Patator
   [37] Hydra
   [38] ChangeMe
   [39] wappalyzer
   [40] builtwith
   [41] wafw00f
   [42] assetnote
   [43] jsbeautifier
   [44] LinkFinder
   [45] MobSF
   [46] GenyMotion
   [47] Apktool
   [48] dex2jar
   [49] jd-gui
   [50] idb
    
    """)
    print("   [99] - Kembali ke Menu Utama \n")
    choice4 = raw_input("   Reyy Project~# ")
    if choice4 == "1":
        clearScr()
        xssradar()
    if choice4 == "2":
        clearScr()
        xsshunter()
    if choice4 == "3":
        clearScr()
        xsshunterclient()
    if choice4 == "4":
        clearScr()
        domxss()
    if choice4 == "5":
        clearScr()
        xsser()
    if choice4 == "6":
        clearScr()
        brutexss()
    if choice4 == "7":
        clearScr()
        xsstrike()
    if choice4 == "8":
        clearScr()
        xssor()
    if choice4 == "9":
        clearScr()
        sqlmap()
    if choice4 == "10":
        clearScr()
        oxmlxxe()
    if choice4 == "11":
        clearScr()
        xeeinj()
    if choice4 == "12":
        clearScr()
        tplmap()
    if choice4 == "13":
        clearScr()
        ssrfdetector()
    if choice4 == "14":
        clearScr()
        groundcontrol()
    if choice4 == "15":
        clearScr()
        lfisuit()
    if choice4 == "16":
        clearScr()
        genxbinavi()
    if choice4 == "17":
        clearScr()
        gittools()
    if choice4 == "18":
        clearScr()
        dvcsripper()
    if choice4 == "19":
        clearScr()
        tkosubs()
    if choice4 == "20":
        clearScr()
        subbruteforcer()
    if choice4 == "21":
        clearScr()
        secondorder()
    if choice4 == "22":
        clearScr()
        racetheweb()
    if choice4 == "23":
        clearScr()
        corstest()
    if choice4 == "24":
        clearScr()
        rcestrutspwn()
    if choice4 == "25":
        clearScr()
        ysoserial()
    if choice4 == "26":
        clearScr()
        phpggc()
    if choice4 == "27":
        clearScr()
        retirejs()
    if choice4 == "28":
        clearScr()
        getsploit()
    if choice4 == "29":
        clearScr()
        findsploit()
    if choice4 == "30":
        clearScr()
        bfac()
    if choice4 == "31":
        clearScr()
        wpscann()
    if choice4 == "32":
        clearScr()
        cmsmap()
    if choice4 == "33":
        clearScr()
        joomscan()
    if choice4 == "34":
        clearScr()
        jsonwtt()
    if choice4 == "35":
        clearScr()
        wfuzz()
    if choice4 == "36":
        clearScr()
        patator()
    if choice4 == "37":
        clearScr()
        hydra()
    if choice4 == "38":
        clearScr()
        changeme()
    if choice4 == "39":
        clearScr()
        wappalyzer()
    if choice4 == "40":
        clearScr()
        builtwith()
    if choice4 == "41":
        clearScr()
        wafwoof()
    if choice4 == "42":
        clearScr()
        assetnote()
    if choice4 == "43":
        clearScr()
        jsbeautifier()
    if choice4 == "44":
        clearScr()
        linkfinder()
    if choice4 == "45":
        clearScr()
        mobsf()
    if choice4 == "46":
        clearScr()
        genymotion()
    if choice4 == "47":
        clearScr()
        apktool()
    if choice4 == "48":
        clearScr()
        dex2jar()
    if choice4 == "49":
        clearScr()
        jdgui()
    if choice4 == "50":
        clearScr()
        idb()
    if choice4 == "99":
        clearScr()
        menu()
    elif choice4 == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

# Reporting ###################################################################

def reporting():
    clearScr()
    print(bughunterlogo)
    print("""
    PoCs & Reporting | Mood Bahasa Indonesia
    ----------------------------------------------------------------
        
    [1] - Platform Bounty Bug
    [2] - POC (Bukti Konsep)
    [3] - Contekan
    [4] - Saksi mata
    [5] - HttpScreenshot
    [6] - BugBountyTemplat
    [7] - Pembuat Templat
    """)    
    print("   [99] - Kembali ke Menu Utama \n")
    choice5 = raw_input("   Reyy Project~# ")
    if choice5 == "tips":
     clearScr()
     bugtips()
    if choice5 == "1":
        clearScr()
        platforms()
    if choice5 == "2":
        clearScr()
        pocs()
    if choice5 == "3":
        clearScr()
        cheatsheet()
    if choice5 == "4":
     clearScr()
     eyewitness()
    if choice5 == "5":
     clearScr()
     httpscreenshot()
    if choice5 == "6":
     clearScr()
     bbtemplates()
    if choice5 == "7":
     clearScr()
     gentemplates()
    elif choice5 == "99":
        menu()
    elif choice5 == "":
        reporting()
    else:
        reporting()

# reyy ########################################################################

def sage():
    clearScr()
    print(bughunterlogo)
    print("""
    Tools by Akbarbarz | Mood Bahasa Indonesia
    ----------------------------------------------------------------
    
    [1] - Hacktronian - Kumpulan Alat Peretasan untuk Unix
    [2] - Hackdroid - 250+ Aplikasi Pengujian Penetrasi untuk Android
    [3] - Hacknix - Alat Peretasan Untuk Semua OS Berbasis Debian
    [4] - Fluxion - Cracker WPA/WPA2 Menggunakan Evil Twin Attack
    [5] - Ducky 4 Arduino - Skrip Ducky untuk Arduino Leonardo Mini
    [6] - DoS dan DDoS - Alat Serangan & Perlindungan
    [7] - Kali-WSL - Mode GUI di Kali Linux Windows
    [8] - HackPi - Mesin Peretasan Portabel dengan RPi3
    [9] - TorFi - Anonymous WiFi Hotspot
    """)
    print("   [99] - Kembali ke Menu Utama \n")
    choicesage = raw_input("   Reyy Project~# ")
    if choicesage == "1":
        clearScr()
        hacktronian()
    if choicesage == "2":
        clearScr()
        hackdroid()
    if choicesage == "3":
        clearScr()
        hacknix()
    if choicesage == "4":
     clearScr()
     fluxion()
    if choicesage == "5":
     clearScr()
     duckydino()
    if choicesage == "6":
     clearScr()
     ddos()
    if choicesage == "7":
     clearScr()
     kaliwsl()
    if choicesage == "8":
     clearScr()
     hackpi()     
    if choicesage == "9":
     clearScr()
     torfi()
    elif choicesage == "99":
        clearScr()
        menu()
    elif choicesage == "":
        clearScr()
        sage()
    else:
        clearScr()
        sage()

# Memperbarui ######################################################################

def updatebughunter():
    os.system('clear')
    print(bughunterlogo)
    print (""" update Bughunter Mood Bahasa Indonesia Ke Versi Terbaru.. Versi Saat Ini: 1.0
    
    Periksa Versi Terbaru Di Sini: https://github.com/Rediawan
    """)
    choiceupdate = raw_input(" Tekan Enter dan Kembali Ke Menu Utama : ")
    if choiceupdate == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()

# Tentang #######################################################################

def about():
    os.system('clear')
    print(bughunterlogo)
    print ("""
---------------------------------------------------------------------
    BugHunter v1.0 | Mood Bahasa Indonesia
---------------------------------------------------------------------
    Unduh Direktori: 
    
    Pengguna Normal : /home/$USER/bughunter/
    
    Pengguna Root : /root/bughunter/
   
    ~/bughunter/info/ : Alat untuk Pengumpulan Informasi
    ~/bughunter/mapp/ : Alat untuk Pemetaan    
    ~/bughunter/disc/ : Alat untuk Penemuan
    ~/bughunter/expt/ : Alat untuk Eksploitasi
    ~/bughunter/rept/ : Alat untuk Pelaporan
    ~/bughunter/reyy/ : Tools by Venom Reyy

    Perhatian : Lihat File README.md untuk Petunjuk Instalasi dan Panduan Cara Penggunaan.
---------------------------------------------------------------------
    Link Media sosial Kami Bisa Cek Di Bawah
 
    Blog      :  https://venomccybersecurity.blogspot.com/
    Github    :  https://github.com/Akbarbarz
    YouTube   :  M.Akbar.B
    Twitter   :  Gk Punya
    Instagram :  _m.akbar_b
---------------------------------------------------------------------
[!] Terima Kasih Telah Menggunakan Tools ini
---------------------------------------------------------------------
    """)
    choiceabout = raw_input(" Tekan Enter dan Kembali Ke Menu Utama : ")
    if choiceabout == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()

# My Info #####################################################################

def myinfo():
    os.system('clear')
    print(bughunterlogo)
    os.system("curl ipinfo.io")
    choicemyinfo = raw_input("\n Tekan Enter dan Kembali Ke Menu Utama : ")
    if choicemyinfo == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()

# SAGE ########################################################################

def hacktronian():
    os.system('clear')
    print ("""
    Kumpulan Alat Peretasan untuk Unix.
    
    Baca Selengkapnya: https://github.com/Rediawan/hacktronian
    """)
    choicehacktronian = raw_input(" Apakah Anda Ingin Mengunduh? Hacktronian? (Y/N) : ")
    if choicehacktronian in yes:
        os.system("cd ~/bughunter/sage/ && git clone https://github.com/thehackingsage/hacktronian.git")
    elif choicehacktronian in no:
      clearScr()
      sage()
    elif choicehacktronian == "":
         clearScr()
         sage()
    else:
         clearScr()
         sage()

def hackdroid():
    os.system('clear')
    print ("""
    HackDroid adalah kumpulan 250+ Pengujian Penetrasi dan Peretasan Etis Aplikasi untuk Android ... dalam hal ini, Aplikasi dibagi menjadi berbeda kategori sehingga Anda dapat Mengunduh Aplikasi apa pun dari 
    
    Baca Selengkapnya: https://github.com/Rediawan/HackDroid
    """)
    choicehackdroid = raw_input(" Apakah Anda Ingin Mengunduh? Hackdroid? (Y/N) : ")
    if choicehackdroid in yes:
        os.system("firefox https://github.com/thehackingsage/HackDroid")
    elif choicehackdroid in no:
      clearScr()
      sage()
    elif choicehackdroid == "":
         clearScr()
         sage()
    else:
         clearScr()
         sage()

def hacknix():
    os.system('clear')
    print ("""
    Hacknix adalah skrip yang menginstal semua alat Kali Linux di sistem operasi berbasis Debian Anda. Yang Anda butuhkan hanyalah Python 2.7 dan paket Git yang terinstal di sistem Anda. Dengan menggunakan skrip ini, Anda dapat menambahkan
    
    Baca Selengkapnya: https://github.com/Rediawan/hacknix
    """)
    choicehacknix = raw_input(" Apakah Anda Ingin Mengunduh? Hacknix? (Y/N) : ")
    if choicehacknix in yes:
        os.system("cd ~/bughunter/sage/ && git clone https://github.com/thehackingsage/hacknix.git")
    elif choicehacknix in no:
      clearScr()
      sage()
    elif choicehacknix == "":
         clearScr()
         sage()
    else:
         clearScr()
         sage()    

def fluxion():
    os.system('clear')
    print(""" 
    Fluxion adalah cracker kunci wifi menggunakan serangan kembar jahat.. Anda memerlukan adaptor nirkabel untuk alat ini.
    
    Baca Selengkapnya: https://github.com/Rediawan/Fluxion
    """)
    choicefluxion = raw_input(" Apakah Anda Ingin Mengunduh? Fluxion? (Y/N) : ")
    if choicefluxion in yes:
        os.system("cd ~/bughunter/sage/ && git clone https://github.com/thehackingsage/Fluxion.git")
    elif choicefluxion in no:
         clearScr()
         sage()
    elif choicefluxion == "":
         clearScr()
         sage()
    else:
         clearScr()
         sage()

def duckydino():
    os.system('clear')
    print ("""
    Skrip Ducky untuk Arduino Leonardo Mini & Arduino Uno + Muatan ke Konverter Arduino
    
    Baca Selengkapnya: https://github.com/Rediawan/ducky4arduino
    """)
    choiceduckydino = raw_input(" Do You Want To Use DuckyDino? (Y/N) : ")
    if choiceduckydino in yes:
        os.system("firefox https://github.com/thehackingsage/ducky4arduino")
    elif choiceduckydino in no:
      clearScr()
      sage()
    elif choiceduckydino == "":
         clearScr()
         sage()
    else:
         clearScr()
         sage()

def ddos():
    os.system('clear')
    print ("""
    Alat Serangan & Perlindungan DoS dan DDoS untuk Windows, Linux & Android 
    
    !!! Untuk Tujuan Pendidikan Saja!!!
    
    Baca Selengkapnya: https://github.com/Rediawan/DDoS
    """)
    choiceddos = raw_input(" Apakah Anda Ingin Mengunduh? DoS & DDoS Tools? (Y/N) : ")
    if choiceddos in yes:
        os.system("cd ~/bughunter/sage/ && git clone https://github.com/thehackingsage/DDoS.git")
    elif choiceddos in no:
      clearScr()
      sage()
    elif choiceddos == "":
         clearScr()
         sage()
    else:
         clearScr()
         sage()

def kaliwsl():
    os.system('clear')
    print ("""
    Alat untuk Aplikasi Windows Kali Linux:
    Perbarui, Tingkatkan, XFCE4 - Mode GUI & Alat Peretasan..
    
    Setelah Mengaktifkan WSL dan Menginstal Aplikasi Kali Linux
    dari Microsoft Store di Windows 10, Jalankan Script Ini. 
    
    Baca Selengkapnya: https://github.com/Rediawan/Kali-WSL.git
    """)
    choicekaliwsl = raw_input(" Apakah Anda Ingin Mengunduh? Kali-WSL? (Y/N) : ")
    if choicekaliwsl in yes:
        os.system("cd ~/bughunter/sage/ && git clone https://github.com/thehackingsage/Kali-WSL.git")
    elif choicekaliwsl in no:
      clearScr()
      sage()
    elif choicekaliwsl == "":
         clearScr()
         sage()
    else:
         clearScr()
         sage()

def hackpi():
    os.system('clear')
    print ("""
    Plug and Play Portable Hacking Machine with RPi3
    
    Update, Upgrade, AutoLogin, AutoVNC & Hacking Tools
    
    Baca Selengkapnya: https://github.com/Rediawan/HackPi
    """)
    choicehackpi = raw_input(" Apakah Anda Ingin Mengunduh? HackPi? (Y/N) : ")
    if choicehackpi in yes:
        os.system("cd ~/bughunter/sage/ && git clone https://github.com/thehackingsage/HackPi.git")
    elif choicehackpi in no:
      clearScr()
      sage()
    elif choicehackpi == "":
         clearScr()
         sage()
    else:
         clearScr()
         sage()

def torfi():
    os.system('clear')
    print ("""
    Anonymous WiFi Hotspot Using Raspberry Pi 3
    
    Baca Selengkapnya: https://github.com/Rediawan/TorFi
    """)
    choicehackpi = raw_input(" Apakah Anda Ingin Mengunduh? TorFi? (Y/N) : ")
    if choicehackpi in yes:
        os.system("cd ~/bughunter/sage/ && git clone https://github.com/thehackingsage/torFi.git")
    elif choicehackpi in no:
      clearScr()
      sage()
    elif choicehackpi == "":
         clearScr()
         sage()
    else:
         clearScr()
         sage()

# Information Gathering #######################################################

def basiccmd():
    os.system('clear')
    print ("""
    use the following steps to validate ownership of a target :

    Ping the target domains/hosts :
    ping google.com 
    ping 8.8.8.8
    
    Whois the target domains/hosts/ip :
    whois example.com
    whois 104.27.178.12
    
    Resolve the IP addresses for the target domains/hosts :
    dig +short example.com
    
    Results could be mixed depending on whether or not the target 
    is using whois privacy protection.
    """)
    choicebasiccmd = raw_input(" Press Enter and Go Back To Information Gathering Menu : ")
    if choicebasiccmd == "":
         clearScr()
         info()
    else:
        clearScr()
        info()
    
def masscan():
    os.system('clear')
    print ("""
    Mass IP port scanner. ... It can scan the entire Internet in under 6 minutes, 
    transmitting 10 million packets per second.
    """)
    choicemasscan = raw_input(" Apakah Anda Ingin Mengunduh? MASSCAN? (Y/N) : ")
    if choicemasscan in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/robertdavidgraham/masscan.git")
    elif choicemasscan in no:
      clearScr()
      info()
    elif choicemasscan == "":
         clearScr()
         info()
    else:
         clearScr()
         info()
         
def dnsrecon():
    os.system('clear')
    print ("""
    DNSRecon is a Python port of a Ruby script that I wrote to learn the language 
    and about DNS in early 2007. This time I wanted to learn about Python and extend 
    the functionality of the original tool and in the process re-learn how DNS works 
    and how could it be used in the process of a security assessment and network troubleshooting.
    """)
    choicednsrecon = raw_input(" Apakah Anda Ingin Mengunduh? DNS-Recon? (Y/N) : ")
    if choicednsrecon in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/darkoperator/dnsrecon.git")
    elif choicednsrecon in no:
      clearScr()
      info()
    elif choicednsrecon == "":
         clearScr()
         info()
    else:
         clearScr()           
         info()
            
def sublister():
    os.system('clear')
    print ("""
    Sublist3r is a python tool designed to enumerate subdomains of websites using OSINT.
    It helps penetration testers and bug hunters collect and gather subdomains for the 
    domain they are targeting. Sublist3r enumerates subdomains using many search engines 
    such as Google, Yahoo, Bing, Baidu, and Ask. Sublist3r also enumerates subdomains 
    using Netcraft, Virustotal, ThreatCrowd, DNSdumpster, and ReverseDNS.
    """)
    choicesublister = raw_input(" Apakah Anda Ingin Mengunduh? SubList3r? (Y/N) : ")
    if choicesublister in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/aboul3la/Sublist3r.git")
    elif choicesublister in no:
      clearScr()
      info()
    elif choicesublister == "":
         clearScr()
         info()
    else:
         clearScr()
         info()

def altdns():
    os.system('clear')
    print ("""
    Altdns is a DNS recon tool that allows for the discovery of subdomains that conform to patterns.
    Altdns takes in words that could be present in subdomains under a domain (such as test, dev, 
    staging) as well as takes in a list of subdomains that you know of..

    From these two lists that are provided as input to altdns, the tool then generates a massive 
    output of "altered" or "mutated" potential subdomains that could be present. It saves this output 
    so that it can then be used by your favourite DNS bruteforcing tool.

    Alternatively, the -r flag can be passed to altdns so that once this output is generated, 
    the tool can then resolve these subdomains (multi-threaded) and save the results to a file.

    Altdns works best with large datasets. Having an initial dataset of 200 or more subdomains should 
    churn out some valid subdomains via the alterations generated.
    """)
    choicealtdns = raw_input(" Apakah Anda Ingin Mengunduh? Altdns? (Y/N) : ")
    if choicealtdns in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/infosec-au/altdns.git")
    elif choicealtdns in no:
      clearScr()
      info()
    elif choicealtdns == "":
         clearScr()
         info()
    else:
         clearScr()
         info()

def amass():
    os.system('clear')
    print ("""
    Amass is a tool for In-Depth DNS Enumeration and Network Mapping..
    """)
    choiceamass = raw_input(" Apakah Anda Ingin Mengunduh? Amass? (Y/N) : ")
    if choiceamass in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/caffix/amass.git")
    elif choiceamass in no:
      clearScr()
      info()
    elif choiceamass == "":
         clearScr()
         info()
    else:
         clearScr()
         info()

def subfinder():
    os.system('clear')
    print ("""
    SubFinder is a subdomain discovery tool that discovers valid subdomains for websites. 
    Designed as a passive framework to be useful for bug bounties and safe for penetration testing.
    """)
    choicesubfinder = raw_input(" Apakah Anda Ingin Mengunduh? Subfinder? (Y/N) : ")
    if choicesubfinder in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/subfinder/subfinder.git")
    elif choicesubfinder in no:
      clearScr()
      info()
    elif choicesubfinder == "":
         clearScr()
         info()
    else:
         clearScr()
         info()

def enumall():
    os.system('clear')
    print ("""
    Recon-ng and Alt-DNS are awesome. This script combines the power of these 
    tools with the ability to run multiple domains within the same session.
    """)
    choiceenumall = raw_input(" Apakah Anda Ingin Mengunduh? Enumall? (Y/N) : ")
    if choiceenumall in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/jhaddix/domain.git && mv domain enumall")
    elif choiceenumall in no:
      clearScr()
      info()
    elif choiceenumall == "":
         clearScr()
         info()
    else:
         clearScr()
         info()

def aquatone():
    os.system('clear')
    print ("""
    Aquatone is a tool for visual inspection of websites across a large amount of hosts 
    and is convenient for quickly gaining an overview of HTTP-based attack surface.
    """)
    choiceaquatone = raw_input(" Apakah Anda Ingin Mengunduh? Aquatone? (Y/N) : ")
    if choiceaquatone in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/michenriksen/aquatone.git")
    elif choiceaquatone in no:
      clearScr()
      info()
    elif choiceaquatone == "":
         clearScr()
         info()
    else:
         clearScr()
         info()

def cloudenum():
    os.system('clear')
    print ("""
    A simple tool to allow easy querying of Cloudflare's DNS data written in Python.
    """)
    choicecloudenum = raw_input(" Apakah Anda Ingin Mengunduh? Cloudflare Enumeration Tool? (Y/N) : ")
    if choicecloudenum in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/mandatoryprogrammer/cloudflare_enum.git")
    elif choicecloudenum in no:
      clearScr()
      info()
    elif choicecloudenum == "":
         clearScr()
         info()
    else:
         clearScr()
         info()

def infog():
    os.system('clear')
    print ("""
    A Information Gethering Tool by LinuxChoice.
    """)
    choiceinfog = raw_input(" Apakah Anda Ingin Mengunduh? InfoG? (Y/N) : ")
    if choiceinfog in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/thelinuxchoice/infog.git")
    elif choiceinfog in no:
      clearScr()
      info()
    elif choiceinfog == "":
         clearScr()
         info()
    else:
         clearScr()
         info()

def harvester():
    os.system('clear')
    print ("""
    theHarvester is a tool for gathering subdomain names, e-mail addresses, 
    virtual hosts, open ports/ banners, and employee names from different 
    public sources (search engines, pgp key servers).
    """)
    choiceharvester = raw_input(" Apakah Anda Ingin Mengunduh? The Harvester? (Y/N) : ")
    if choiceharvester in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/laramies/theHarvester.git")
    elif choiceharvester in no:
      clearScr()
      info()
    elif choiceharvester == "":
         clearScr()
         info()
    else:
         clearScr()
         info()

def reconng():
    os.system('clear')
    print ("""
    One of The Best Reconnaissance Tool.. (and my personal favourite) 
    """)
    choicereconng = raw_input(" Apakah Anda Ingin Mengunduh? Recon-ng? (Y/N) : ")
    if choicereconng in yes:
        os.system("cd ~/bughunter/info/ && git clone https://LaNMaSteR53@bitbucket.org/LaNMaSteR53/recon-ng.git")
    elif choicereconng in no:
      clearScr()
      info()
    elif choicereconng == "":
         clearScr()
         info()
    else:
         clearScr()
         info()

def setoolkit():
    os.system('clear')
    print ("""
    The Social-Engineer Toolkit is an open-source penetration testing framework
    designed for social engineering. SET has a number of custom attack vectors that
    allow you to make a believable attack quickly.
    """)
    choicesetoolkit = raw_input(" Apakah Anda Ingin Mengunduh? Setoolkit (Y/N) : ")
    if choicesetoolkit in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/trustedsec/social-engineer-toolkit.git")
    elif choicesetoolkit in no:
        clearScr()
        info()
    elif choicesetoolkit == "":
        clearScr()
        info()
    else:
        clearScr()
        info()

def whatweb():
    os.system('clear')
    print ("""
    WhatWeb identifies websites. Its goal is to answer the question, "What is that Website?". 
    WhatWeb recognises web technologies including content management systems (CMS), blogging 
    platforms, statistic/analytics packages, JavaScript libraries, web servers, and embedded 
    devices. WhatWeb has over 1700 plugins, each to recognise something different. WhatWeb 
    also identifies version numbers, email addresses, account IDs, web framework modules, 
    SQL errors, and more.
    """)
    choicewhatweb = raw_input(" Apakah Anda Ingin Mengunduh? WhatWeb? (Y/N) : ")
    if choicewhatweb in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/urbanadventurer/WhatWeb.git")
    elif choicewhatweb in no:
      clearScr()
      info()
    elif choicewhatweb == "":
         clearScr()
         info()
    else:
         clearScr()
         info()

def maltego():
    os.system('clear')
    print ("""
    Maltego is proprietary software used for open-source intelligence and forensics, 
    developed by Paterva. Maltego focuses on providing a library of transforms for 
    discovery of data from open sources, and visualizing that information in a graph 
    format, suitable for link analysis and data mining. 
    """)
    choicemaltego = raw_input(" Apakah Anda Ingin Mengunduh? Maltego? (Y/N) : ")
    if choicemaltego in yes:
        os.system("firefox https://www.paterva.com/web7/downloads.php")
    elif choicemaltego in no:
      clearScr()
      info()
    elif choicemaltego == "":
         clearScr()
         info()
    else:
         clearScr()
         info()
         
def goohak():
    os.system("clear")
    print ("""
    Automatically launch google hacking queries against a target domain to find 
    vulnerabilities and enumerate a target.
    """)
    choicegoohak = raw_input (" Apakah Anda Ingin Mengunduh? Goohak? (Y/N) : ")
    if choicegoohak in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/1N3/Goohak.git")
    elif choicegoohak in no:
      clearScr()
      info()
    elif choicegoohak == "":
         clearScr()
         info()
    else:
         clearScr()
         info()
         
def googdorker():
    os.system("clear")
    print ("""
    GoogD0rker is a tool for firing off google dorks against a target domain, 
    it is purely for OSINT against a specific target domain. It is split into 
    two versions, a bash script designed for OSX and a python script designed 
    to be cross platform.
    """)
    choicegoogdorker = raw_input (" Apakah Anda Ingin Mengunduh? Googdorker? (Y/N) : ")
    if choicegoogdorker in yes:
        os.system("cd ~/bughunter/info/ && git clone https://github.com/ZephrFish/GoogD0rker.git")
    elif choicegoogdorker in no:
      clearScr()
      info()
    elif choicegoogdorker == "":
         clearScr()
         info()
    else:
         clearScr()
         info()

def usefullinks():
    os.system("clear")
    print ("""
    Some Useful Links for Reconnaissance & Enumeration..
    
    Wayback Machine         : https://web.archive.org/
    Wayback Robots          : https://gist.github.com/mhmdiaa/2742c5e147d49a804b408bfed3d32d07
    Wayback URLs            : https://gist.github.com/mhmdiaa/adf6bff70142e5091792841d4b372050
    Shodan                  : https://shodan.io/
    Internet Wide Scan Data : http://Repositoryscans.io/
    Censys                  : https://censys.io/
    Hurricane Electric      : http://bgp.he.net/
    Netcraft                : https://www.netcraft.com/
    DomainCrawler           : http://www.domaincrawler.com/
    W3DT                    : https://w3dt.net/
    Netinfo                 : http://www.netinfo.org.ua
    DomainSearch            : http://domainsearch.com/
    DomainTools             : http://whois.domaintools.com/
    InterNIC                : http://www.internic.net/whois.html
    Who.IS                  : http://www.who.is/
    Whois.net               : http://www.whois.net/
    Visual Traceroute       : http://en.dnstools.ch/port-scan.html
    CentralOps.net          : http://centralops.net/co/
    DNS Stuff               : http://www.dnsstuff.com/
    IP-Address              : http://www.ip-adress.com/
    IPinfo Security Portal  : http://ipinfo.info/index.php
    Internet Domain Survey  : http://www.isc.org/index.pl?/ops/ds/
    NerdLabs                : http://www.nerdlabs.org/tools/
    NetQuery                : http://www.ipaddress123.com/nquser.php
    Network Tools           : http://home.planet.nl/~houwe135/wbnt1/
    Network Tools 2         : http://www.network-tools.com/
    RobTex SwissArmyKnife   : https://www.robtex.com/
    WebTic DNS scan         : http://tools.webtic.nl/dnsscan
    Geo IP Tool             : http://geoiptool.com/
    Geographic Location     : http://tejji.com/ip/
    Reverse IP domain check : http://www.yougetsignal.com/tools/web-s ... eb-server/
    Internet Traffic Report : http://www.internettrafficreport.com/europe.htm
    """)
    choiceusefullinks = raw_input (" Press Enter and Go Back To Information Gathering Menu : ")
    if choiceusefullinks == "":
         clearScr()
         info()
    else:
         clearScr()
         info()
         
# Mapping #####################################################################

def nmap():
    os.system('clear')
    print ("""
    Nmap is a free and open-source security scanner, originally written by Gordon Lyon, 
    used to discover hosts and services on a computer network, thus building a "map" of 
    the network. To accomplish its goal, Nmap sends specially crafted packets to the 
    target host and then analyzes the responses. It's a TCP/IP host and port scanning 
    tool with fantastic service and OS fingerprinting capabilities.
    """)
    choicenmap = raw_input(" Apakah Anda Ingin Mengunduh? Nmap? (Y/N) : ")
    if choicenmap in yes:
        os.system("cd ~/bughunter/mapp/ && git clone https://github.com/nmap/nmap.git")
    elif choicenmap in no:
        clearScr()
        mapping()
    elif choicenmap == "":
        clearScr()
        mapping()
    else:
        clearScr()
        mapping()

def firefox():
    clearScr()
    print ("""
    Mozilla Firefox is a free and open-source web browser. 
    
    https://www.mozilla.org/en-US/firefox/new/
    
    """)
    choicefirefox = raw_input(" Apakah Anda Ingin Mengunduh? Firefox? (Y/N) : ")
    if choicefirefox in yes:
        os.system("sudo apt-get install firefox")
    elif choicefirefox in no:
        clearScr()
        mapping()
    elif choicefirefox == "":
        clearScr()
        mapping()
    else:
        clearScr()
        mapping()

def firefoxext():
    clearScr()
    print ("""
    A tool that transforms Firefox browsers into a penetration testing suite.
    
    """)
    choicefirefoxext = raw_input(" Apakah Anda Ingin Mengunduh? Firefox Pentesting Extensions? (Y/N) : ")
    if choicefirefoxext in yes:
        os.system("cd ~/bughunter/mapp && git clone https://github.com/mazen160/Firefox-Security-Toolkit.git")
    elif choicefirefoxext in no:
        clearScr()
        mapping()
    elif choicefirefoxext == "":
        clearScr()
        mapping()
    else:
        clearScr()
        mapping()

def burpsuitepro():
    os.system('clear')
    print (""" 
    Burp Suite is a Java based Web Penetration Testing framework.
    It has become an industry standard suite of tools used by information security
    professionals. Burp Suite helps you identify vulnerabilities and verify attack
    vectors that are affecting web applications.
    
    BurpSuite Pro v1.6.67 : https://github.com/thehackingsage/burpsuite.git\n
    """)
    choiceburp = raw_input(" Apakah Anda Ingin Mengunduh? BurpSuite Pro v1.6.67 (Y/N) : ")
    if choiceburp in yes:
        os.system("firefox https://github.com/thehackingsage/burpsuite.git")
    elif choiceburp in no:
      clearScr()
      mapping()
    elif choiceburp == "":
         clearScr()
         mapping()
    else:
        clearScr()
        mapping()

def burpext():
    os.system('clear')
    print ("""
    You Can Use All Extensions From BApp Store in Burp Suite Pro..
 
    Most Useful Extensions : 
 
    Backslash Powered Scanner, Reflected Parameters, SAML Encoder/Decoder,
    Bypass WAF, CVSS Calculator, Java deserialization Scanner, Autorize,
    BurpSmartBuster, Content Type Converter, JSON Beautifier, PsychoPATH,
    Retire-js, J2EEScan, SAML Raider, Active Scan ++, UUID Detector, Wsdler, 
    Additional Scanner Checks, CO2 Flow, Hackvertor, Meth0dMan & Paramalyzer.
 
    Burp Suite Pro v1.6.67 : https://github.com/thehackingsage/burpsuite.git
    """)
    choiceburpext = raw_input("\n Tekan Enter dan Kembali Ke Menu Utama : ")
    if choiceburpext == "":
         clearScr()
         mapping()
    else:
        clearScr()
        mapping()

def intruderpayload():
    clearScr()
    print ("""
    A collection of Burpsuite Intruder payloads, BurpBounty payloads, fuzz lists, 
    malicious file uploads and web pentesting methodologies and checklists. 
    """)
    choiceintruderpayload = raw_input(" Apakah Anda Ingin Mengunduh? IntruderPayloads? (Y/N) : ")
    if choiceintruderpayload in yes:
        os.system("cd ~/bughunter/mapp/ && git clone https://github.com/1N3/IntruderPayloads.git")
    elif choiceintruderpayload in no:
        clearScr()
        mapping()
    elif choiceintruderpayload == "":
        clearScr()
        mapping()
    else:
        clearScr()
        mapping()
    
def allpayload():
    clearScr()
    print ("""
    A list of useful payloads and bypass for Web Application Security and Pentest/CTF
    """)
    choiceallpayload = raw_input(" Apakah Anda Ingin Mengunduh? PayloadsAllTheThings? (Y/N) : ")
    if choiceallpayload in yes:
        os.system("cd ~/bughunter/mapp/ && git clone https://github.com/swisskyrepo/PayloadsAllTheThings.git")
    elif choiceallpayload in no:
        clearScr()
        mapping()
    elif choiceallpayload == "":
        clearScr()
        mapping()
    else:
        clearScr()
        mapping()
    
def gitallsec():
    clearScr()
    print ("""
    A tool to capture all the git secrets by leveraging multiple open source git searching tools
    """)
    choicegitallsec = raw_input(" Apakah Anda Ingin Mengunduh? Git-all-Secrets? (Y/N) : ")
    if choicegitallsec in yes:
        os.system("cd ~/bughunter/mapp/ && git clone https://github.com/anshumanbh/git-all-secrets.git")
    elif choicegitallsec in no:
        clearScr()
        mapping()
    elif choicegitallsec == "":
        clearScr()
        mapping()
    else:
        clearScr()
        mapping()
    
# Discovery ###################################################################

def acunetix():
    clearScr()
    print ("""
    Acunetix is the leading web vulnerability scanner used by serious Fortune 500 companies 
    and widely acclaimed to include the most advanced SQL injection and XSS black box scanning 
    technology. It automatically crawls your websites and performs black box AND grey box hacking 
    techniques which finds dangerous vulnerabilities that can compromise your website and data.
    """)
    choiceacunetix = raw_input(" Apakah Anda Ingin Mengunduh? Acunetix Web Vulnerability Scanner? (Y/N) : ")
    if choiceacunetix in yes:
        os.system("firefox https://www.acunetix.com/vulnerability-scanner/download/")
    elif choiceacunetix in no:
        clearScr()
        discovery()
    elif choiceacunetix == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()
    
def arachni():
    clearScr()
    print ("""
    Arachni is a feature-full, modular, high-performance Ruby framework aimed towards helping 
    penetration testers and administrators evaluate the security of modern web applications.
    """)
    choicearachni = raw_input(" Apakah Anda Ingin Mengunduh? Arachni Web Vulnerability Scanner? (Y/N) : ")
    if choicearachni in yes:
        os.system("firefox http://www.arachni-scanner.com/download/")
    elif choicearachni in no:
        clearScr()
        discovery()
    elif choicearachni == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()
        
def burpsuite():
    clearScr()
    print ("""
    Burp or Burp Suite is a graphical tool for testing Web application security. 
    The tool is written in Java and developed by PortSwigger Web Security. 
    """)
    choiceburpsuite = raw_input(" Apakah Anda Ingin Mengunduh? Burp Suite Community Edition? (Y/N) : ")
    if choiceburpsuite in yes:
        os.system("firefox https://portswigger.net/burp/communitydownload")
    elif choiceburpsuite in no:
        clearScr()
        discovery()
    elif choiceburpsuite == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def nexpose():
    clearScr()
    print ("""
    Rapid7 Nexpose is a vulnerability scanner which aims to support the entire vulnerability 
    management lifecycle, including discovery, detection, verification, risk classification, 
    impact analysis, reporting and mitigation. It integrates with Rapid7's Metasploit for 
    vulnerability exploitation.
    """)
    choicenexpose = raw_input(" Apakah Anda Ingin Mengunduh? Nexpose? (Y/N) : ")
    if choicenexpose in yes:
        os.system("firefox https://www.rapid7.com/products/nexpose/download/")
    elif choicenexpose in no:
        clearScr()
        discovery()
    elif choicenexpose == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def nikto():
    clearScr()
    print ("""
    Nikto is an Open Source (GPL) web server scanner which performs comprehensive
    tests against web servers for multiple items, including over 6400 potentially 
    dangerous files/CGIs, checks for outdated versions of over 1200 servers, 
    and version specific problems on over 270 servers.

    """)
    choicenikto = raw_input(" Apakah Anda Ingin Mengunduh? Nikto? (Y/N) : ")
    if choicenikto in yes:
        os.system("cd ~/bughunter/disc/ && git clone https://github.com/sullo/nikto.git")
    elif choicenikto in no:
        clearScr()
        discovery()
    elif choicenikto == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def vega():
    clearScr()
    print ("""
    Vega is a free and open source web security scanner and web security testing platform 
    to test the security of web applications. Vega can help you find and validate SQL Injection, 
    Cross-Site Scripting (XSS), inadvertently disclosed sensitive information, and other vulnerabilities.
    """)
    choicevega = raw_input(" Apakah Anda Ingin Mengunduh? Vega? (Y/N) : ")
    if choicevega in yes:
        os.system("firefox https://subgraph.com/vega/download/")
    elif choicevega in no:
        clearScr()
        discovery()
    elif choicevega == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def wapiti():
    clearScr()
    print ("""
    Wapiti is a vulnerability scanner for web applications. It currently search vulnerabilities 
    like XSS, SQL and XPath injections, file inclusions, command execution, XXE injections, 
    CRLF injections, Server Side Request Forgery... It use the Python 3 programming language.
    """)
    choicewapiti = raw_input(" Apakah Anda Ingin Mengunduh? Wapiti? (Y/N) : ")
    if choicewapiti in yes:
        os.system("cd ~/bughunter/disc/ && wget https://sourceforge.net/projects/wapiti/files/wapiti/wapiti-3.0.1/wapiti3-3.0.1.zip")
    elif choicewapiti in no:
        clearScr()
        discovery()
    elif choicewapiti == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def websecscan():
    clearScr()
    discovery()

def websecsuite():
    clearScr()
    print ("""
    Fully integrated web-based platform to manage vulnerabilities across security teams, 
    investigating security breaches, or test for vulnerabilities.
    """)
    choicewebsecsuite = raw_input(" Do You Want To Use Security Suite? (Y/N) : ")
    if choicewebsecsuite in yes:
        os.system("firefox https://secapps.com/suite")
    elif choicewebsecsuite in no:
        clearScr()
        discovery()
    elif choicewebsecsuite == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def joomscan():
    clearScr()
    print ("""
    OWASP Joomla! Vulnerability Scanner (JoomScan) is an open source project, developed with the aim 
    of automating the task of vulnerability detection and reliability assurance in Joomla CMS deployments. 
    Implemented in Perl, this tool enables seamless and effortless scanning of Joomla installations, 
    while leaving a minimal footprint with its lightweight and modular architecture. It not only detects 
    known offensive vulnerabilities, but also is able to detect many misconfigurations and admin-level 
    shortcomings that can be exploited by adversaries to compromise the system. Furthermore, OWASP JoomScan 
    provides a user-friendly interface and compiles the final reports in both text and HTML formats for 
    ease of use and minimization of reporting overheads. 
    """)
    choicejoomscan = raw_input(" Apakah Anda Ingin Mengunduh? JoomScan? (Y/N) : ")
    if choicejoomscan in yes:
        os.system("cd ~/bughunter/disc/ && git clone https://github.com/rezasp/joomscan.git")
    elif choicejoomscan in no:
        clearScr()
        discovery()
    elif choicejoomscan == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def waaaf():
    clearScr()
    print ("""
    w3af is an open source web application security scanner which helps developers and penetration testers 
    identify and exploit vulnerabilities in their web applications. The scanner is able to identify 200+ 
    vulnerabilities, including Cross-Site Scripting, SQL injection and OS commanding.
    """)
    choicewaaaf = raw_input(" Apakah Anda Ingin Mengunduh? W3AF? (Y/N) : ")
    if choicewaaaf in yes:
        os.system("cd ~/bughunter/disc/ && git clone https://github.com/andresriancho/w3af.git")
    elif choicewaaaf in no:
        clearScr()
        discovery()
    elif choicewaaaf == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def zed():
    clearScr()
    print ("""
    OWASP ZAP is an open-source web application security scanner. It is intended to be used 
    by both those new to application security as well as professional penetration testers. 
    It is one of the most active OWASP projects and has been given Flagship status.
    """)
    choicezed = raw_input(" Apakah Anda Ingin Mengunduh? Wapiti? (Y/N) : ")
    if choicezed in yes:
        os.system("cd ~/bughunter/disc/ && wget https://github.com/zaproxy/zaproxy/releases/download/w2018-12-10/ZAP_WEEKLY_D-2018-12-10.zip")
    elif choicezed in no:
        clearScr()
        discovery()
    elif choicezed == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def wpscan():
    clearScr()
    print ("""
    WPScan is a free, for non-commercial use, black box WordPress vulnerability scanner written 
    for security professionals and blog maintainers to test the security of their sites. 
    https://www.wpscan.org
    """)
    choicewpscan = raw_input(" Apakah Anda Ingin Mengunduh? WP-Scan? (Y/N) : ")
    if choicewpscan in yes:
        os.system("cd ~/bughunter/disc/ && git clone https://github.com/wpscanteam/wpscan.git")
    elif choicewpscan in no:
        clearScr()
        discovery()
    elif choicewpscan == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def fuzzdb():
    clearScr()
    print ("""
    FuzzDB was created to increase the likelihood of causing and identifying conditions of security
    interest through dynamic application security testing. It's the first and most comprehensive 
    open dictionary of fault injection patterns, predictable resource locations, and regex for 
    matching server responses.
    """)
    choicefuzzdb = raw_input(" Apakah Anda Ingin Mengunduh? FuzzDB? (Y/N) : ")
    if choicefuzzdb in yes:
        os.system("cd ~/bughunter/disc/ && git clone https://github.com/fuzzdb-project/fuzzdb.git")
    elif choicefuzzdb in no:
        clearScr()
        discovery()
    elif choicefuzzdb == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def cewl():
    clearScr()
    print ("""
    CeWL is a Custom Word List Generator
    """)
    choicecewl = raw_input(" Apakah Anda Ingin Mengunduh? CeWL? (Y/N) : ")
    if choicecewl in yes:
        os.system("cd ~/bughunter/disc/ && git clone https://github.com/digininja/CeWL.git")
    elif choicecewl in no:
        clearScr()
        discovery()
    elif choicecewl == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def dirbuster():
    clearScr()
    print ("""
    DirBuster is a multi threaded java application designed to brute force directories 
    and files names on web/application servers.
    """)
    choicedirbuster = raw_input(" Apakah Anda Ingin Mengunduh? DirBuster? (Y/N) : ")
    if choicedirbuster in yes:
        os.system("firefox https://sourceforge.net/projects/dirbuster/")
    elif choicedirbuster in no:
        clearScr()
        discovery()
    elif choicedirbuster == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def dirb():
    clearScr()
    print ("""
    DIRB is a Web Content Scanner. It looks for existing (and/or hidden) Web Objects.
    It basically works by launching a dictionary based attack against a web server 
    and analizing the response.
    """)
    choicedirb = raw_input(" Apakah Anda Ingin Mengunduh? DIRB? (Y/N) : ")
    if choicedirb in yes:
        os.system("cd ~/bughunter/disc/ && wget https://sourceforge.net/projects/dirb/files/dirb/2.22/dirb222.tar.gz")
    elif choicedirb in no:
        clearScr()
        discovery()
    elif choicedirb == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def filebuster():
    clearScr()
    print ("""
    An extremely fast and flexible web fuzzer.
    """)
    choicefilebuster = raw_input(" Apakah Anda Ingin Mengunduh? FileBuster? (Y/N) : ")
    if choicefilebuster in yes:
        os.system("cd ~/bughunter/disc/ && git clone https://github.com/henshin/filebuster.git")
    elif choicefilebuster in no:
        clearScr()
        discovery()
    elif choicefilebuster == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def gobuster():
    clearScr()
    print ("""
    GoBuster is a tool used to brute-force URIs in web sites and DNS subdomains (with wildcard support).
    """)
    choicegobuster = raw_input(" Apakah Anda Ingin Mengunduh? GoBuster? (Y/N) : ")
    if choicegobuster in yes:
        os.system("cd ~/bughunter/disc/ && git clone https://github.com/OJ/gobuster.git")
    elif choicegobuster in no:
        clearScr()
        discovery()
    elif choicegobuster == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

def dirsearch():  
    clearScr()
    print ("""
    Dirsearch is a simple command line tool designed to brute force directories and files in websites.
    """)
    choicedirsearch = raw_input(" Apakah Anda Ingin Mengunduh? Wapiti? (Y/N) : ")
    if choicedirsearch in yes:
        os.system("cd ~/bughunter/disc/ && git clone https://github.com/maurosoria/dirsearch.git")
    elif choicedirsearch in no:
        clearScr()
        discovery()
    elif choicedirsearch == "":
        clearScr()
        discovery()
    else:
        clearScr()
        discovery()

# Exploitation ################################################################

def xssradar():
    clearScr()
    print ("""
    XSS Radar is a tool that detects parameters and fuzzes them for cross-site scripting vulnerabilities.
    """)
    choicexssradar = raw_input(" Apakah Anda Ingin Mengunduh? XSS Radar? (Y/N) : ")
    if choicexssradar in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/bugbountyforum/XSS-Radar.git")
    elif choicexssradar in no:
        clearScr()
        exploit()
    elif choicexssradar == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def xsshunter():
    clearScr()
    print ("""
    XSS Hunter allows you to find all kinds of cross-site scripting vulnerabilities, including the 
    often-missed blind XSS. The service works by hosting specialized XSS probes which, upon firing, 
    scan the page and send information about the vulnerable page to the XSS Hunter service..
    
    Create an XSS Hunter account at https://xsshunter.com/
    """)
    choicexsshunter = raw_input(" Apakah Anda Ingin Mengunduh? XSS Hunter? (Y/N) : ")
    if choicexsshunter in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/mandatoryprogrammer/xsshunter")
    elif choicexsshunter in no:
        clearScr()
        exploit()
    elif choicexsshunter == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()
    
def xsshunterclient():
    clearScr()
    print ("""
    This tool can be used to generate correlated XSS payloads, these payloads are tagged with a unique 
    ID which can be used to track which HTTP request caused which XSS payload to fire. By using this tool 
    all of your injection attempts are tracked and the reports you generate will have the responsible 
    injection attempt included in the final output. This is useful since XSS payloads can often traverse 
    multiple services (and even protocols) before firing, so it's not always clear what injection caused 
    a certain XSS payload to fire.
    """)
    choicexsshunterclient = raw_input(" Apakah Anda Ingin Mengunduh? XSS Hunter Client? (Y/N) : ")
    if choicexsshunterclient in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/mandatoryprogrammer/xsshunter_client.git")
    elif choicexsshunterclient in no:
        clearScr()
        exploit()
    elif choicexsshunterclient == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def domxss():
    clearScr()
    print ("""
    DOM XSS Scanner is an online tool that facilitates code review of web pages and JavaScript code 
    for potential DOM based XSS security vulnerabilities.
    """)
    choicedomxss = raw_input(" Apakah Anda Ingin Mengunduh? DOM XSS Scanner? (Y/N) : ")
    if choicedomxss in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/yaph/domxssscanner.git")
    elif choicedomxss in no:
        clearScr()
        exploit()
    elif choicedomxss == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()
    
def xsser():
    clearScr()
    print ("""
    Cross Site "Scripter" (aka XSSer) is an automatic -framework- to detect, exploit and report XSS vulnerabilities.
    """)
    choicexsser = raw_input(" Apakah Anda Ingin Mengunduh? XSSer? (Y/N) : ")
    if choicexsser in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/epsylon/xsser.git")
    elif choicexsser in no:
        clearScr()
        exploit()
    elif choicexsser == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def brutexss():
    clearScr()
    print ("""
    Cross-Site Scripting BruteForcer 
    """)
    choicebrutexss = raw_input(" Apakah Anda Ingin Mengunduh? BruteXSS? (Y/N) : ")
    if choicebrutexss in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/rajeshmajumdar/BruteXSS.git")
    elif choicebrutexss in no:
        clearScr()
        exploit()
    elif choicebrutexss == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def xsstrike():
    clearScr()
    print("""
    XSStrike is a python script designed to detect and exploit XSS vulnerabilites.
    """)
    choicexsstrike = raw_input(" Apakah Anda Ingin Mengunduh? XSStrike (Y/N) : ")
    if choicexsstrike in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/UltimateHackers/XSStrike.git && cd XSStrike && chmod +x * && pip install -r requirements.txt && clear && python xsstrike")
    elif choicexsstrike in no:
      clearScr()
      exploit()
    elif choicexsstrike == "":
         clearScr()
         exploit()
    else:
        clearScr()
        exploit()
        
def xssor():
    clearScr()
    print ("""
    XSSOR contains three major modules: Encode/Decode, Codz, Probe. Try Online Version: http://xssor.io
    """)
    choicexssor = raw_input(" Apakah Anda Ingin Mengunduh? XSSor? (Y/N) : ")
    if choicexssor in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/evilcos/xssor2.git")
    elif choicexssor in no:
        clearScr()
        exploit()
    elif choicexssor == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()
        
def sqlmap():
    clearScr()
    print ("""
    Automatic SQL injection and database takeover tool. http://sqlmap.org
    """)
    choicesqlmap = raw_input ( "Apakah Anda Ingin Mengunduh? Sqlmap? (Y/N) : ")
    if choicesqlmap in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/sqlmapproject/sqlmap.git")
    elif choicesqlmap in no:
        clearScr()
        exploit()
    elif choicesqlmap == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def oxmlxxe():
    clearScr()
    print ("""
    A tool for embedding XXE/XML exploits into different filetypes.
    """)
    choiceoxmlxxe = raw_input(" Apakah Anda Ingin Mengunduh? OXML-XXE? (Y/N) : ")
    if choiceoxmlxxe in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/BuffaloWill/oxml_xxe.git")
    elif choiceoxmlxxe in no:
        clearScr()
        exploit()
    elif choiceoxmlxxe == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def xeeinj():
    clearScr()
    print ("""
    XXEinjector automates retrieving files using direct and out of band methods.
    Directory listing only works in Java applications. Bruteforcing method needs to be used for other applications.
    """)
    choicexeeinj = raw_input(" Apakah Anda Ingin Mengunduh? XXEinjector? (Y/N) : ")
    if choicexeeinj in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/enjoiz/XXEinjector.git")
    elif choicexeeinj in no:
        clearScr()
        exploit()
    elif choicexeeinj == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def tplmap():
    clearScr()
    print ("""
    Server-Side Template Injection and Code Injection Detection and Exploitation Tool.
    """)
    choicetplmap = raw_input(" Apakah Anda Ingin Mengunduh? Tplmap? (Y/N) : ")
    if choicetplmap in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/epinna/tplmap.git")
    elif choicetplmap in no:
        clearScr()
        exploit()
    elif choicetplmap == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def ssrfdetector():
    clearScr()
    print ("""
    Server-side request forgery detector.
    """)
    choicessrfdetector = raw_input(" Apakah Anda Ingin Mengunduh? SSRF-Detector? (Y/N) : ")
    if choicessrfdetector in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/JacobReynolds/ssrfDetector.git")
    elif choicessrfdetector in no:
        clearScr()
        exploit()
    elif choicessrfdetector == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def groundcontrol():
    clearScr()
    print ("""
    A collection of scripts that run on my web server. Mainly for debugging SSRF, blind XSS, and XXE vulnerabilities.
    """)
    choicegroundcontrol = raw_input(" Apakah Anda Ingin Mengunduh? Ground Control? (Y/N) : ")
    if choicegroundcontrol in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/jobertabma/ground-control.git")
    elif choicegroundcontrol in no:
        clearScr()
        exploit()
    elif choicegroundcontrol == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def lfisuit():
    clearScr()
    print ("""
    Totally Automatic LFI Exploiter (+ Reverse Shell) and Scanner.
    """)
    choicelfisuit = raw_input(" Apakah Anda Ingin Mengunduh? LFISuit? (Y/N) : ")
    if choicelfisuit in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/D35m0nd142/LFISuite.git")
    elif choicelfisuit in no:
        clearScr()
        exploit()
    elif choicelfisuit == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def genxbinavi():
    clearScr()
    print ("""
    File uploader.
    """)
    choicegenxbinavi = raw_input(" Apakah Anda Ingin Mengunduh? Gen-xbin-Avi? (Y/N) : ")
    if choicegenxbinavi in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/neex/ffmpeg-avi-m3u-xbin.git")
    elif choicegenxbinavi in no:
        clearScr()
        exploit()
    elif choicegenxbinavi == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def gittools():
    clearScr()
    print ("""
    A repository with 3 tools for pwn'ing websites with .git repositories available.
    """)
    choicegittools = raw_input(" Apakah Anda Ingin Mengunduh? GitTools? (Y/N) : ")
    if choicegittools in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/internetwache/GitTools.git")
    elif choicegittools in no:
        clearScr()
        exploit()
    elif choicegittools == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def dvcsripper():
    clearScr()
    print ("""
    Rip web accessible (distributed) version control systems: SVN/GIT/HG...
    """)
    choicedvcsripper = raw_input(" Apakah Anda Ingin Mengunduh? DVSC Ripper? (Y/N) : ")
    if choicedvcsripper in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/kost/dvcs-ripper.git")
    elif choicedvcsripper in no:
        clearScr()
        exploit()
    elif choicedvcsripper == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def tkosubs():
    clearScr()
    print ("""
    A tool that can help detect and takeover subdomains with dead DNS records
    """)
    choicetkosubs = raw_input(" Apakah Anda Ingin Mengunduh? tko-subs? (Y/N) : ")
    if choicetkosubs in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/anshumanbh/tko-subs.git")
    elif choicetkosubs in no:
        clearScr()
        exploit()
    elif choicetkosubs == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def subbruteforcer():
    clearScr()
    print ("""
    This app will bruteforce for exisiting subdomains and provide the IP address and Host information.
    """)
    choicesubbruteforcer = raw_input(" Apakah Anda Ingin Mengunduh? HostileSubBruteforcer? (Y/N) : ")
    if choicesubbruteforcer in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/nahamsec/HostileSubBruteforcer.git")
    elif choicesubbruteforcer in no:
        clearScr()
        exploit()
    elif choicesubbruteforcer == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def secondorder():
    clearScr()
    print ("""
    Second-order subdomain takeover scanner.
    """)
    choicesecondorder = raw_input(" Apakah Anda Ingin Mengunduh? Second-Order? (Y/N) : ")
    if choicesecondorder in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/mhmdiaa/second-order.git")
    elif choicesecondorder in no:
        clearScr()
        exploit()
    elif choicesecondorder == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def racetheweb():
    clearScr()
    print ("""
    Tests for race conditions in web applications. Includes a RESTful API to integrate into a continuous integration pipeline. http://RaceTheWeb.io
    """)
    choiceracetheweb = raw_input(" Apakah Anda Ingin Mengunduh? Race The Web? (Y/N) : ")
    if choiceracetheweb in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/insp3ctre/race-the-web.git")
    elif choiceracetheweb in no:
        clearScr()
        exploit()
    elif choiceracetheweb == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def corstest():
    clearScr()
    print ("""
    A simple CORS misconfiguration scanner.
    """)
    choicecorstest = raw_input(" Apakah Anda Ingin Mengunduh? CORStest? (Y/N) : ")
    if choicecorstest in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/RUB-NDS/CORStest.git")
    elif choicecorstest in no:
        clearScr()
        exploit()
    elif choicecorstest == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def rcestrutspwn():
    clearScr()
    print ("""
    An exploit for Apache Struts CVE-2017-5638.
    """)
    choicercestrutspwn = raw_input(" Apakah Anda Ingin Mengunduh? RCE struts-pwn? (Y/N) : ")
    if choicercestrutspwn in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/mazen160/struts-pwn.git")
    elif choicercestrutspwn in no:
        clearScr()
        exploit()
    elif choicercestrutspwn == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def ysoserial():
    clearScr()
    print ("""
    A proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization.
    """)
    choiceysoserial = raw_input(" Apakah Anda Ingin Mengunduh? Y-So-Serial? (Y/N) : ")
    if choiceysoserial in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/GoSecure/ysoserial.git")
    elif choiceysoserial in no:
        clearScr()
        exploit()
    elif choiceysoserial == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def phpggc():
    clearScr()
    print ("""
    PHPGGC is a library of unserialize() payloads along with a tool to generate them, from command line or programmatically. 
    """)
    choicephpggc = raw_input(" Apakah Anda Ingin Mengunduh? PHP Generic Gadget Chains? (Y/N) : ")
    if choicephpggc in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/ambionics/phpggc.git")
    elif choicephpggc in no:
        clearScr()
        exploit()
    elif choicephpggc == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def retirejs():
    clearScr()
    print ("""
    scanner detecting the use of JavaScript libraries with known vulnerabilities.
    http://retirejs.github.io/retire.js/
    """)
    choiceretirejs = raw_input(" Apakah Anda Ingin Mengunduh? Retire.js? (Y/N) : ")
    if choiceretirejs in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/RetireJS/retire.js.git")
    elif choiceretirejs in no:
        clearScr()
        exploit()
    elif choiceretirejs == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def getsploit():
    clearScr()
    print ("""
    Command line utility for searching and downloading exploits.
    """)
    choicegetsploit = raw_input(" Apakah Anda Ingin Mengunduh? Getsploit? (Y/N) : ")
    if choicegetsploit in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/vulnersCom/getsploit.git")
    elif choicegetsploit in no:
        clearScr()
        exploit()
    elif choicegetsploit == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def findsploit():
    clearScr()
    print ("""
    Find exploits in local and online databases instantly. https://crowdshield.com
    """)
    choicefindsploit = raw_input(" Apakah Anda Ingin Mengunduh? Findsploit? (Y/N) : ")
    if choicefindsploit in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/1N3/Findsploit.git")
    elif choicefindsploit in no:
        clearScr()
        exploit()
    elif choicefindsploit == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def bfac():
    clearScr()
    print ("""
    BFAC (Backup File Artifacts Checker): An automated tool that checks for backup artifacts
    that may disclose the web-application's source code.
    """)
    choicebfac = raw_input(" Apakah Anda Ingin Mengunduh? BFAC? (Y/N) : ")
    if choicebfac in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/mazen160/bfac.git")
    elif choicebfac in no:
        clearScr()
        exploit()
    elif choicebfac == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def wpscann():
    clearScr()
    print ("""
    WPScan is a free, for non-commercial use, black box WordPress vulnerability scanner
    written for security professionals and blog maintainers to test the security of their sites.
    https://www.wpscan.org
    """)
    choicewpscann = raw_input(" Apakah Anda Ingin Mengunduh? WPScan? (Y/N) : ")
    if choicewpscann in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/wpscanteam/wpscan.git")
    elif choicewpscann in no:
        clearScr()
        exploit()
    elif choicewpscann == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def cmsmap():
    clearScr()
    print ("""
    CMSmap is a python open source CMS scanner that automates the process of detecting 
    security flaws of the most popular CMSs.
    """)
    choicecmsmap = raw_input(" Apakah Anda Ingin Mengunduh? CMSmap? (Y/N) : ")
    if choicecmsmap in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/Dionach/CMSmap.git")
    elif choicecmsmap in no:
        clearScr()
        exploit()
    elif choicecmsmap == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def joomscan():
    clearScr()
    print ("""
    OWASP Joomla Vulnerability Scanner Project.
    https://www.owasp.org/index.php/Category:OWASP_Joomla_Vulnerability_Scanner_Project
    """)
    choicejoomscan = raw_input(" Apakah Anda Ingin Mengunduh? Joomscan? (Y/N) : ")
    if choicejoomscan in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/rezasp/joomscan.git")
    elif choicejoomscan in no:
        clearScr()
        exploit()
    elif choicejoomscan == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def jsonwtt():
    clearScr()
    print ("""
    A toolkit for testing, tweaking and cracking JSON Web Tokens
    """)
    choicejsonwtt = raw_input(" Apakah Anda Ingin Mengunduh? The JSON Web Token Toolkit? (Y/N) : ")
    if choicejsonwtt in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/ticarpi/jwt_tool.git")
    elif choicejsonwtt in no:
        clearScr()
        exploit()
    elif choicejsonwtt == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def wfuzz():
    clearScr()
    print ("""
    Web application fuzzer. http://wfuzz.org
    """)
    choicewfuzz = raw_input(" Apakah Anda Ingin Mengunduh? Wfuzz? (Y/N) : ")
    if choicewfuzz in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/xmendez/wfuzz.git")
    elif choicewfuzz in no:
        clearScr()
        exploit()
    elif choicewfuzz == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def patator():
    clearScr()
    print ("""
    Patator is a multi-purpose brute-forcer, with a modular design and a flexible usage.
    """)
    choicepatator = raw_input(" Apakah Anda Ingin Mengunduh? Patator? (Y/N) : ")
    if choicepatator in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/lanjelot/patator.git")
    elif choicepatator in no:
        clearScr()
        exploit()
    elif choicepatator == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def hydra():
    clearScr()
    print ("""
    This tool is a proof of concept code, to give researchers and security consultants
    the possibility to show how easy it would be to gain unauthorized access from remote to a system.
    """)
    choicehydra = raw_input(" Apakah Anda Ingin Mengunduh? Hydra? (Y/N) : ")
    if choicehydra in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/vanhauser-thc/thc-hydra.git")
    elif choicehydra in no:
        clearScr()
        exploit()
    elif choicehydra == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def changeme():
    clearScr()
    print ("""
    A default credential scanner.
    """)
    choicechangeme = raw_input(" Apakah Anda Ingin Mengunduh? ChangeMe? (Y/N) : ")
    if choicechangeme in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/ztgrace/changeme.git")
    elif choicechangeme in no:
        clearScr()
        exploit()
    elif choicechangeme == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def wappalyzer():
    clearScr()
    print ("""
    Wappalyzer is a cross-platform utility that uncovers the technologies used on websites.
    It detects content management systems, ecommerce platforms, web frameworks, 
    server software, analytics tools and many more.
    """)
    choicewappalyzer = raw_input(" Do You Want To Visit Wappalyzer? (Y/N) : ")
    if choicewappalyzer in yes:
        os.system("firefox https://wappalyzer.com")
    elif choicewappalyzer in no:
        clearScr()
        exploit()
    elif choicewappalyzer == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def builtwith():
    clearScr()
    print ("""
    Find out what websites are Built With.
    """)
    choicebuiltwith = raw_input(" Do You Want To Visit BuiltWith? (Y/N) : ")
    if choicebuiltwith in yes:
        os.system("firefox https://builtwith.com/")
    elif choicebuiltwith in no:
        clearScr()
        exploit()
    elif choicebuiltwith == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def wafwoof():
    clearScr()
    print ("""
    WAFW00F allows one to identify and fingerprint Web Application Firewall (WAF) products protecting a website.
    """)
    choicewafwoof = raw_input(" Apakah Anda Ingin Mengunduh? WAFW00F? (Y/N) : ")
    if choicewafwoof in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/EnableSecurity/wafw00f.git")
    elif choicewafwoof in no:
        clearScr()
        exploit()
    elif choicewafwoof == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def assetnote():
    clearScr()
    print ("""
    Assetnote is a subdomains supervision tools which allow for real-time notifications 
    about newlly added subdomains.
    """)
    choiceassetnote = raw_input(" Apakah Anda Ingin Mengunduh? AssetNote? (Y/N) : ")
    if choiceassetnote in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/infosec-au/assetnote")
    elif choiceassetnote in no:
        clearScr()
        exploit()
    elif choiceassetnote == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def jsbeautifier():
    clearScr()
    print ("""
    Beautifier for javascript. https://beautifier.io
    """)
    choicejsbeautifier = raw_input(" Apakah Anda Ingin Mengunduh? JavaScript Beautifier? (Y/N) : ")
    if choicejsbeautifier in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/beautify-web/js-beautify.git")
    elif choicejsbeautifier in no:
        clearScr()
        exploit()
    elif choicejsbeautifier == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def linkfinder():
    clearScr()
    print ("""
    A python script that finds endpoints in JavaScript files.
    """)
    choicelinkfinder = raw_input(" Apakah Anda Ingin Mengunduh? LinkFinder? (Y/N) : ")
    if choicelinkfinder in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/GerbenJavado/LinkFinder.git")
    elif choicelinkfinder in no:
        clearScr()
        exploit()
    elif choicelinkfinder == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def mobsf():
    clearScr()
    print ("""
    Mobile Security Framework is an automated, all-in-one mobile application (Android/iOS/Windows)
    pen-testing framework capable of performing static analysis, dynamic analysis, malware analysis 
    and web API testing. https://opensecurity.in
    """)
    choicemobsf = raw_input(" Apakah Anda Ingin Mengunduh? Mobile-Security-Framework? (Y/N) : ")
    if choicemobsf in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/MobSF/Mobile-Security-Framework-MobSF.git")
    elif choicemobsf in no:
        clearScr()
        exploit()
    elif choicemobsf == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def genymotion():
    clearScr()
    print ("""
    Android Emulator.
    """)
    choicegenymotion = raw_input(" Apakah Anda Ingin Mengunduh? GenyMotion? (Y/N) : ")
    if choicegenymotion in yes:
        os.system("firefox https://www.genymotion.com/")
    elif choicegenymotion in no:
        clearScr()
        exploit()
    elif choicegenymotion == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def apktool():
    clearScr()
    print ("""
    A tool for reverse engineering Android apk files.
    """)
    choiceapktool = raw_input(" Apakah Anda Ingin Mengunduh? APKTool? (Y/N) : ")
    if choiceapktool in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/iBotPeaches/apktool.git")
    elif choiceapktool in no:
        clearScr()
        exploit()
    elif choiceapktool == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def dex2jar():
    clearScr()
    print ("""
    Tools to work with android .dex and java .class files.
    """)
    choicedex2jar = raw_input(" Apakah Anda Ingin Mengunduh? dex2jar? (Y/N) : ")
    if choicedex2jar in yes:
        os.system("firefox https://sourceforge.net/projects/dex2jar/files/dex2jar-2.0.zip/download")
    elif choicedex2jar in no:
        clearScr()
        exploit()
    elif choicedex2jar == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def jdgui():
    clearScr()
    print ("""
    A standalone graphical utility that displays Java sources from CLASS files.
    """)
    choicejdgui = raw_input(" Apakah Anda Ingin Mengunduh? JD-GUI? (Y/N) : ")
    if choicejdgui in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/java-decompiler/jd-gui.git")
    elif choicejdgui in no:
        clearScr()
        exploit()
    elif choicejdgui == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

def idb():
    clearScr()
    print ("""
    idb is a tool to simplify some common tasks for iOS pentesting and research. 
    Originally there was a command line version of the tool, but it is no longer 
    under development so you should get the GUI version. http://www.idbtool.com/
    """)
    choiceidb = raw_input(" Apakah Anda Ingin Mengunduh? idb? (Y/N) : ")
    if choiceidb in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/dmayer/idb.git")
    elif choiceidb in no:
        clearScr()
        exploit()
    elif choiceidb == "":
        clearScr()
        exploit()
    else:
        clearScr()
        exploit()

# Reporting ###################################################################

def bugtips():
    os.system('clear')
    print ("""
    Tips for Bug Hunting | https://thehackingsage.github.io
    -----------------------------------------------------------
    
    * Always Read The Source Code.
    * Get Subdomains and Start with Unpopuler Domains. 
    * Always Check The Backend CMS & Backend Language.
    * Use Google Dorks.
    * Check Each Request and Response.
    * Active Mind - Think Out of The Box. ;)
    """)
    choicebugtips = raw_input(" Press Enter and Go Back To Menu : ")
    if choicebugtips == "":
        clearScr()
        reporting()
    else:
        clearScr()
        reporting()

def platforms():
    os.system('clear')
    print (""" 
    Bug Bounty Platforms | https://thehackingsage.github.io
    -----------------------------------------------------------
    
    Bugcrowd : https://bugcrowd.com/
    Hackerone : https://hackerone.com/    
    Google : https://google.com/about/appsecurity/    
    Facebook : https://facebook.com/BugBounty/
    Open Bug Bounty : https://www.openbugbounty.org/ 
    HackTrophy : https://hacktrophy.com/
    BountyGraph : https://bountygraph.com/
    PlugBounty : https://www.plugbounty.com/
    intigriti : https://www.intigriti.com/
    SlowMist : https://www.slowmist.com/
    Synack : https://synack.com/    
    Japan Bug bounty Program : https://bugbounty.jp/    
    Cobalt : https://cobalt.io/    
    Zerocopter : https://zerocopter.com/    
    Hackenproof : https://hackenproof.com/    
    BountyFactory : https://bountyfactory.io    
    AntiHack : https://www.antihack.me/    
    
    More Bug Bounty Programs List : https://bugcrowd.com/bug-bounty-list/\n
    """)
    choiceplatforms = raw_input(" Press Enter and Go Back To Menu : ")
    if choiceplatforms == "":
        clearScr()
        reporting()
    else:
        clearScr()
        reporting()
        
def pocs():
    os.system('clear')
    print (""" 
    Proof of Concepts and Write-Ups from Other Hackers..
    -----------------------------------------------------------
    
    Bug Bounty write-ups : https://forum.bugcrowd.com/t/researcher-resources-bounty-bug-write-ups/
    Awesome Bug Bounty : https://github.com/djadmin/awesome-bug-bounty
    SecurityBreached-BugBounty POC : https://blog.securitybreached.org/category/bugbounty-poc/
    Facebook Hunting POC : https://m.facebook.com/notes/phwd/facebook-bug-bounties/707217202701640/?__tn__=%2As-R
    Bug Hunting Tutorials : https://forum.bugcrowd.com/t/researcher-resources-tutorials/370
    PentesterLand Bug Bounty Writeups : https://pentester.land/list-of-bug-bounty-writeups.html
    Hackerone POC Reports : http://h1.nobbd.de/
    Bug Bounty POC : http://www.xsses.com/
    Netsec on Reddit : https://www.reddit.com/r/netsec
    Bug Bounty World : https://bugbountyworld.com/\n
    """)
    choiceplatforms = raw_input(" Press Enter and Go Back To Menu : ")
    if choiceplatforms == "":
        clearScr()
        reporting()
    else:
        clearScr()
        reporting()

def cheatsheet():
    os.system('clear')
    print (""" 
    Cheat Sheets for Bug Hunting | https://thehackingsage.github.io
    -----------------------------------------------------------------
    
    Pentest Bookmarks : https://github.com/kurobeats/pentest-bookmarks/blob/master/BookmarksList.md
    Awesome OSINT Cheat-Sheet : https://github.com/jivoi/awesome-osint
    Awesome Pentest Cheat-Sheet : https://github.com/enaqx/awesome-pentest
    Bug Bounty Cheat-Sheet : https://github.com/EdOverflow/bugbounty-cheatsheet
    Awesome Hacking Cheat-Sheet : https://github.com/Hack-with-Github/Awesome-Hacking
    Awesome-Infosec Cheat-Sheet : https://github.com/onlurking/awesome-infose
    SQL Injection Cheat-Sheet : http://pentestmonkey.net/blog/mssql-sql-injection-cheat-sheet/
    XSS Cheat-Sheet : https://gist.github.com/kurobeats/9a613c9ab68914312cbb415134795b45
    XXE Payload : https://gist.github.com/staaldraad/01415b990939494879b4\n
    """)
    choiceplatforms = raw_input(" Press Enter and Go Back To Menu : ")
    if choiceplatforms == "":
        clearScr()
        reporting()
    else:
        clearScr()
        reporting()

def eyewitness():
    clearScr()
    print("""
    EyeWitness is designed to take screenshots of websites, RDP services, and open VNC servers, 
    provide some server header info, and identify default credentials if possible.
    """)
    choiceeyewitness = raw_input(" Apakah Anda Ingin Mengunduh? EyeWitness (Y/N) : ")
    if choiceeyewitness in yes:
        os.system("cd ~/bughunter/repo/ && git clone https://github.com/FortyNorthSecurity/EyeWitness.git")
    elif choiceeyewitness in no:
      clearScr()
      reporting()
    elif choiceeyewitness == "":
         clearScr()
         reporting()
    else:
        clearScr()
        reporting()

def httpscreenshot():
    clearScr()
    print("""
    HTTPScreenshot is a tool for grabbing screenshots and HTML of large numbers of websites.
    The goal is for it to be both thorough and fast which can sometimes oppose each other.
    """)
    choicehttpscreenshot = raw_input(" Apakah Anda Ingin Mengunduh? HTTPScreenshot (Y/N) : ")
    if choicehttpscreenshot in yes:
        os.system("cd ~/bughunter/repo/ && git clone https://github.com/breenmachine/httpscreenshot.git")
    elif choicehttpscreenshot in no:
      clearScr()
      reporting()
    elif choicehttpscreenshot == "":
         clearScr()
         reporting()
    else:
        clearScr()
        reporting()

def bbtemplates():
    clearScr()
    print("""
    A collection of templates for bug bounty reporting, with guides on how to write and fill out.
    """)
    choicebbtemplates = raw_input(" Apakah Anda Ingin Mengunduh? Bug Bounty Templates (Y/N) : ")
    if choicebbtemplates in yes:
        os.system("cd ~/bughunter/repo/ && git clone https://github.com/ZephrFish/BugBountyTemplates.git")
    elif choicebbtemplates in no:
      clearScr()
      reporting()
    elif choicebbtemplates == "":
         clearScr()
         reporting()
    else:
        clearScr()
        reporting()

def gentemplates():
    clearScr()
    print("""
    A simple variable based template editor using handlebarjs+strapdownjs. The idea is to use 
    variables in markdown based files to easily replace the variables with content. Data is 
    saved temporarily in local storage. PHP is only needed to generate the list of files in 
    the dropdown of templates.
    """)
    choicegentemplates = raw_input(" Apakah Anda Ingin Mengunduh? Template Generator (Y/N) : ")
    if choicegentemplates in yes:
        os.system("cd ~/bughunter/expt/ && git clone https://github.com/fransr/template-generator.git")
    elif choicegentemplates in no:
      clearScr()
      reporting()
    elif choicegentemplates == "":
         clearScr()
         reporting()
    else:
        clearScr()
        reporting()

###############################################################################

def clearScr():
    """
    clear the screen in case of GNU/Linux or Windows
    """
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')        

###############################################################################

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(" Finishing Up...\r"),
        os.system("clear")
        time.sleep(0.25)

