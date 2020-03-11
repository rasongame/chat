import socket, sys, os
import threading

def main():
    conn, addr = s.accept()
    users.append(conn)
    while True:
        data, addr = conn.recvfrom(128)
        data_split = data.decode().split(":")
        print(users)
        try:
            print(addr)
            for user in users:
                user.send(f"{data_split[1]}".encode())
        except BrokenPipeError:
            sys.stderr.write("Oops. Client is disconnected")


def init():
    for x in range(16):
        thread = threading.Thread(target=main)
        thread.start()
if __name__ == '__main__':
    try:
        users = []
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", int(sys.argv[1])))
        s.listen(128)
        init()
        s.close()
    except ConnectionResetError:
        sys.stderr.write("Connection reset by peer")
        exit(1)

