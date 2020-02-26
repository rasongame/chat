import socket
from time import sleep
from math import pow
from threading import Thread
import sys
def getUpdates():
    try:
        while True:
            new_msg = sock.recv(4096)
            print(new_msg.decode())
    except KeyboardInterrupt:
        exit()


UDP_PORT = 2965
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect((sys.argv[1], UDP_PORT))
sock.send(f"join".encode())
# promptThread = Thread(target=spawnPrompt)

pollThread = Thread(target=getUpdates)
pollThread.daemon = True
pollThread.start()

while True:
    try:
        msg = input("\r==> ")
        prepared_msg = f"‏‏‎ ‎{msg}"
        sock.send(prepared_msg.encode())
    except KeyboardInterrupt:
        exit()


