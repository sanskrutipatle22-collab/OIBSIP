import socket
import threading


HOST = "127.0.0.1"
PORT = 5555


def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")

            if not message:
                print("\nServer disconnected.")
                break

            print(f"\n{message}")
            print("You: ", end="", flush=True)

        except:
            print("\nDisconnected from server.")
            break


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connect to the server.")
        print("Make sure server.py is running first.")
        return

    print("=" * 45)
    print("        💬 CHAT CLIENT")
    print("=" * 45)

    username = input("Enter your name: ").strip()

    while not username:
        print("Name cannot be empty.")
        username = input("Enter your name: ").strip()

    client.send(username.encode("utf-8"))

    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client,),
        daemon=True
    )

    receive_thread.start()

    print("\nConnected to the chat!")
    print("Type your message and press Enter.")
    print("Type /quit to leave the chat.\n")

    while True:
        try:
            message = input("You: ")

            if message.lower() == "/quit":
                print("Leaving chat...")
                break

            if message.strip():
                client.send(message.encode("utf-8"))

        except (KeyboardInterrupt, EOFError):
            break

    client.close()


if __name__ == "__main__":
    start_client()