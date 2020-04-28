import socket

HEADER_SIZE = 64
PORT = 3000
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
# run server.py to check the ip address and update as required
SERVER_IP_ADDRESS = "192.168.0.102"
REMOTE_ADDRESS = (SERVER_IP_ADDRESS, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(REMOTE_ADDRESS)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER_SIZE - len(send_length))
    client.send(send_length)
    client.send(message)


send("Hello!")
input()
send("How are you?")
input()
send("Thank you, take care!")
input()
send(DISCONNECT_MESSAGE)
