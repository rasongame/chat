import socket
UDP_PORT = 2965

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.connect("localhost")
sock.bind(('', UDP_PORT))
users = []

while True:
    try:
        data, addr = sock.recvfrom(4096)
        if not data: break
        if data.decode() == "join":
            users.append(addr)
            for addr in users:
                sock.sendto(f" {addr[0]} is joined".encode(),addr )

        if data.decode() == "":
            sock.sendto("Dont send blank space messages..",addr)
        print(f"[ {addr[0]} ] : {data.decode()}")
        for addr in users:
            sock.sendto(f"[ {addr[0]} ]: {data.decode()}".encode(), addr)
    except KeyboardInterrupt:
        exit()

sock.close()
