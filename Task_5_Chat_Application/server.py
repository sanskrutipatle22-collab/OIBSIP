import socket
import threading
from datetime import datetime


HOST = "127.0.0.1"
PORT = 5555

clients = []
usernames = {}


def get_time():
    return datetime.now().strftime("%H:%M")


def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode("utf-8"))
            except:
                remove_client(client)


def remove_client(client):
    if client in clients:
        clients.remove(client)

    username = usernames.pop(client, "Unknown")

    message = f"[{get_time()}] System: {username} has disconnected."
    broadcast(message)


def handle_client(client):
    try:
        username = client.recv(1024).decode("utf-8")

        usernames[client] = username
        clients.append(client)

        print(f"{username} connected.")

        welcome_message = (
            f"[{get_time()}] System: {username} has joined the chat."
        )

        print(welcome_message)
        broadcast(welcome_message, client)

        while True:
            message = client.recv(1024).decode("utf-8")

            if not message:
                break

            formatted_message = (
                f"[{get_time()}] {username}: {message}"
            )

            print(formatted_message)
            broadcast(formatted_message, client)

    except ConnectionResetError:
        pass

    finally:
        remove_client(client)
        client.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print("=" * 45)
    print("        💬 CHAT SERVER")
    print("=" * 45)
    print(f"Server running on {HOST}:{PORT}")
    print("Waiting for clients...")
    print("=" * 45)

    while True:
        client, address = server.accept()

        print(f"New connection from {address}")

        thread = threading.Thread(
            target=handle_client,
            args=(client,)
        )

        thread.start()


if __name__ == "__main__":
    start_server()