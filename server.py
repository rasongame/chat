import socket
UDP_PORT = 2965
TCP_PORT = 2966

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.connect("localhost")
sock.bind(('', UDP_PORT))

users = []
SERVICE_WORDS = ["join", "disconnect"]
while True:
    try:
        data, address = sock.recvfrom(4096)
        if not data: break
        if data.decode() == SERVICE_WORDS[0]:
            users.append(address)
            for addr in users:
                sock.sendto(f" {address[0]} is joined".encode(),addr )

        if data.decode() == "":
            sock.sendto("Dont send blank space messages..",addr)
        print(f"[ {address[0]} ] : {data.decode()}")
        if data.decode() == SERVICE_WORDS[1]:
            pass

        for addr in users:
            sock.sendto(f"[ {address[0]} ]: {data.decode()}".encode(), addr)
    except KeyboardInterrupt:
        exit()

sock.close()
