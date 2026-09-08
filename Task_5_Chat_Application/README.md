# 💬 Python Chat Application

A real-time two-user chat application built with Python using socket programming and threading.

This project was developed as part of my **Python Programming Internship – Task 5: Chat Application**.

---

## 📌 Project Overview

This application demonstrates real-time communication between two clients through a Python server.

The server listens for incoming client connections and handles multiple clients using threads. Connected clients can send and receive messages in real time.

The application runs locally using `127.0.0.1` (localhost).

---

## ✨ Features

- 💻 Client-server architecture
- 🔌 Socket-based communication
- 💬 Real-time bidirectional messaging
- 👥 Supports two connected clients
- 🕐 Timestamped messages
- 🔔 Join notifications
- 🚪 Graceful disconnection handling
- 🖥️ Runs completely on localhost
- 🧵 Threading for handling clients simultaneously
- ⚠️ Connection error handling
- 🚫 Empty username validation

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Socket | Network communication |
| Threading | Handling multiple clients |
| Datetime | Message timestamps |

---

## 📂 Project Structure

```text
Chat Application/
│
├── screenshots/
│   ├── Alice-chat.png
│   ├── Bob-chat.png
│   └── server.png
│
├── .gitignore
├── client.py
├── server.py
└── README.md
---

## 🚀 How to Run

### Step 1 — Open the Project

Open the `Chat Application` folder in VS Code.

### Step 2 — Start the Server

Open a terminal and run:

```bash
python server.py
Step 3 — Start Client 1

Open a second terminal and run:

python client.py

Enter a username, for example:

Alice
Step 4 — Start Client 2

Open a third terminal and run:

python client.py

Enter another username:

Bob
Step 5 — Start Chatting

Alice and Bob can now exchange messages in real time.

Example:

[22:07] Alice: Hello Bob!
[22:08] Bob: Hi Alice!
📸 Screenshots
🖥️ Server

The server listens for incoming client connections and handles connected users.

👩 Alice Client

Alice's client showing real-time communication.

👨 Bob Client

Bob's client showing real-time communication.

🔄 Application Architecture
                 💬 CHAT APPLICATION

                      SERVER
                 127.0.0.1:5555
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
          CLIENT 1            CLIENT 2
           Alice                Bob
             │                   │
             └─────────┬─────────┘
                       │
                Real-time messages
🧵 Threading Architecture

The server uses Python's threading module to handle connected clients independently.

                    SERVER
                      │
          ┌───────────┴───────────┐
          │                       │
      Thread 1                Thread 2
          │                       │
        Alice                    Bob
          │                       │
          └───────────┬───────────┘
                      │
                Message Exchange
🕐 Message Format

Messages include the time and username:

[22:07] Alice: Hello Bob!
[22:08] Bob: Hi Alice!

System events are also displayed:

[22:09] System: Bob has joined the chat.
[22:10] System: Bob has disconnected.
🚪 Graceful Disconnection

Users can leave the chat by typing:

/quit

The application closes the client connection and notifies the other user.

Example:

[22:10] System: Bob has disconnected.
📋 Internship Task Checklist
Task 5 — Chat Application
 Server script that listens for incoming client connections
 Client script that connects to the server
 Real-time bidirectional message exchange
 Two-user communication
 Timestamp prefix for messages
 Username displayed with messages
 Graceful disconnection handling
 Notification when a client disconnects
 Both scripts runnable on the same machine
 Uses localhost (127.0.0.1)
 Socket programming
 Threading implementation
 Empty username validation
🧠 What I Learned

Through this project, I learned:

Python socket programming
Client-server architecture
TCP communication
Sending and receiving data
Python threading
Handling multiple clients
Real-time communication
Exception handling
Graceful disconnection
Organizing a Python project
Writing technical documentation
🔮 Future Improvements

Possible future improvements include:

👥 Support for more than two users
🔐 User authentication
🏠 Multiple chat rooms
💾 Message history using SQLite
🖥️ Graphical user interface
📎 File sharing
😀 Emoji support
🔔 Desktop notifications
🌐 Internet-based communication
🔒 Encrypted communication
👩‍💻 Author

Sanskruti Patle

Python Programming Internship — Task 5

📄 License

This project was created for educational and internship purposes.


