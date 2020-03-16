#!/usr/bin/python3

import socket
from time import sleep
from math import pow
from threading import Thread
import sys
from random import randint
def getUpdates():
    try:
        while True:
            new_msg = sock.recv(4096)
            print(new_msg.decode())
    except KeyboardInterrupt:
        exit()

nickname = ""
UDP_PORT = 2965
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
if 2 >= 0 and 2 < len(sys.argv):
    nickname = sys.argv[2]
else:
    nickname = randint(100, 200)
try:
    sock.connect((sys.argv[1], UDP_PORT))
except IndexError:
    raise Exception("Не указан IP.")

sock.send(f"{nickname} : join".encode())
# promptThread = Thread(target=spawnPrompt)

pollThread = Thread(target=getUpdates)
pollThread.daemon = True
pollThread.start()

while True:
    try:
        msg = input("==> ")
        prepared_msg = f"‏‏‎{nickname} : {msg}"
        sock.send(prepared_msg.encode())
    except KeyboardInterrupt:
        sock.send(f"{nickname} : disconnect".encode())
        exit()


