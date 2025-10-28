💬 Flask Local Chat App

A simple local network chat application built using Flask (Python).
It allows two users on the same Wi-Fi or hotspot to chat with each other through their browsers — no internet or database needed.


---

⚙️ Features

Simple two-user chat

Messages auto-saved locally in JSON

Works on both Termux (Android) and Kali Linux / Ubuntu

Clean and responsive chat interface

Manual refresh for new messages



---

🧰 Folder Structure

chat_app/
│
├── chat_server.py        # Main Flask app
│
└── templates/
    ├── index.html        # Chat page UI
    └── login.html        # Username entry page


---

📲 Setup on Termux (Android)

1. Install Python and Flask

pkg update && pkg upgrade -y
pkg install python -y
pip install flask

2. Move your project folder to Termux

mv /sdcard/chat_app /data/data/com.termux/files/home/
cd ~/chat_app

3. Run the chat server

python chat_server.py

You’ll see something like:

* Running on http://0.0.0.0:5000

4. Open on the same phone

Open your browser and go to:

http://127.0.0.1:5000

5. Open on another phone (same Wi-Fi)

Find your Termux IP:

ifconfig

Example:

inet 192.168.43.161

Then open on the other phone:

http://192.168.43.161:5000

Now both phones can chat with each other.


---

💻 Setup on Kali Linux / Ubuntu

1. Install Flask

sudo apt update
sudo apt install python3-pip -y
pip3 install flask

2. Run the app

cd chat_app
python3 chat_server.py

3. Open in browser

http://127.0.0.1:5000

For LAN chat:

http://<your-system-ip>:5000


---

🧠 How It Works

1. chat_server.py runs a local Flask web server.


2. When you log in from login.html, your username is saved.


3. index.html displays chat messages, which are saved in a local JSON file.


4. When one user sends a message, the other can see it by refreshing their page.




---

🔒 Notes

Works only in local networks (no internet).

To stop, press CTRL + C in the terminal.

You can customize HTML/CSS to match your theme.



---

🧾 License

This project is open-source.
You can use or modify it for learning or development purposes.
