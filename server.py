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
        user_data = data.decode().split(":")
        if user_data[1] == SERVICE_WORDS[0]:
            users.append(address)
            for addr in users:
                sock.sendto(f" {user_data[0]} is joined".encode(),addr )

        if user_data[1] == "":
            sock.sendto("Dont send blank space messages..",addr)
        print(f"[ {user_data[0]} ] : {user_data[1]}")
        if user_data[1] == SERVICE_WORDS[1]:
            pass

        for addr in users:
            sock.sendto(f"[ {user_data[0]} ]: {user_data[1]}".encode(), addr)
    except KeyboardInterrupt:
        exit()

sock.close()
