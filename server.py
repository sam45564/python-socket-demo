import socket
import threading

HEADER_SIZE = 64  # in bytes
FORMAT = "utf-8"
PORT = 3000
IP_ADDRESS = socket.gethostbyname(socket.gethostname())
SERVER_ADDRESS = (IP_ADDRESS, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDRESS)


def handle_request(new_connection, client_ip):
    print(f"[SERVER] {client_ip} connected")
    connected = True
    while connected:
        msg_length = new_connection.recv(HEADER_SIZE).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            actual_msg = new_connection.recv(msg_length).decode(FORMAT)
            if actual_msg == DISCONNECT_MESSAGE:
                break

            print(f"[{client_ip}] {actual_msg}")

    new_connection.close()


def start():
    server.listen()
    print(f"[SERVER] Server started at {SERVER_ADDRESS}")
    while True:
        new_connection, client_ip = server.accept()
        thread = threading.Thread(
            target=handle_request, args=(new_connection, client_ip))
        thread.start()
        print(
            f"[SERVER] Total active thread(s): {threading.activeCount() - 1}")


print("[SERVER] Starting...")
start()
