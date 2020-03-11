import socket, sys, os
import threading
from random import randint as random
# import concurrent.futures

def pollThreads(s):
    while True:
        print(s.recv(1024).decode())

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', int(sys.argv[1])))
    pollThread = threading.Thread(target=pollThreads, args=(s,))
    pollThread.daemon = True
    pollThread.start()

    while True:
        data = input("==> ")
        prepared_data = f"{sys.argv[2] or random(1000,2000)}:{data}".encode()
        # data = "space".encode()
        if not prepared_data:
            # sys.stdout.write("blank message")
            pass
        s.send(prepared_data)
    s.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write("KeyboardInterrupt")
        exit(0)
