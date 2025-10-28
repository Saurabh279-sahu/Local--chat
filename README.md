💬 Local Chat app (Flask)

A simple **local chat application** built with Python and Flask that allows two or more users to chat on the same Wi-Fi or hotspot network.  
No external server or internet connection required — just connect devices to the same network and start chatting locally.

---

## 🚀 Features
- Works on both **Termux** and **Kali Linux**
- Chat between multiple devices on the same Wi-Fi or hotspot
- Clean and simple user interface
- Separate sender and receiver message bubbles (like WhatsApp)
- No database required — runs directly on Flask

---

## 📁 Folder Structure
``
chat_app/
│
├── chat_server.py
└── templates/
    ├── index.html
    └── login.html

---

## ⚙️ Installation on Termux

1. **Update and install Python**
   ```bash
   pkg update && pkg upgrade
   pkg install python
   ```
2. Install Flask
```bash
pip install flask
```

3. Move your project folder
Copy your chat_app folder to:
```bash
/data/data/com.termux/files/home/
```

4. Start the server
```bash
cd ~/chat_app
python chat_server.py
```

5. Note the IP address shown, for example:
```bash
Running on http://192.168.43.161:5000
```


6. Open the link

On your own phone: open the given IP in Chrome or any browser

On another device: connect it to the same hotspot/Wi-Fi and open the same IP in browser





---

💻 Installation on Kali Linux

1. Install dependencies
```bash
sudo apt update
sudo apt install python3 python3-pip
pip install flask
```

2. Navigate to your project folder
```bash
cd ~/chat_app
```


3. Run the server
```bash
python3 chat_server.py
```


4. Access the app
Open the displayed local IP address in any browser (on same network).




---

🧠 How It Works

Flask runs a local web server on port 5000

Devices connected to the same network can open the chat in their browser

Messages are exchanged through Flask routes and stored temporarily in memory (RAM)



---

🧩 Troubleshooting

If “This site can’t be reached” appears:
Make sure both devices are connected to the same hotspot/Wi-Fi

If Send button is disabled:
Refresh the page after entering your name in login

Use Chrome or Firefox for best performance



---

👨‍💻 Author

Saurabh Sahu
📍 Created for local network chatting using Flask & Python.
🖥️ Works on mobile, PC, and Kali Linux.


---

📜 License

This project is open-source and free to use for learning purposes.


