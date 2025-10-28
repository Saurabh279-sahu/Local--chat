from flask import Flask, render_template_string, request, redirect, url_for
import datetime

app = Flask(__name__)
messages = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Local Chat</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #e5ddd5;
            margin: 0;
            padding: 0;
        }
        .chat-container {
            width: 100%;
            max-width: 600px;
            margin: auto;
            background: #fff;
            height: 90vh;
            display: flex;
            flex-direction: column;
            border-radius: 10px;
            box-shadow: 0 0 10px #999;
            overflow: hidden;
        }
        .chat-header {
            background: #075E54;
            color: white;
            padding: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
        }
        .chat-messages {
            flex: 1;
            padding: 10px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
        }
        .message {
            max-width: 75%;
            padding: 8px 12px;
            margin: 5px 0;
            border-radius: 15px;
            position: relative;
            word-wrap: break-word;
        }
        .sender {
            background-color: #DCF8C6;
            align-self: flex-start;
            border-bottom-left-radius: 0;
        }
        .receiver {
            background-color: #E1FFC7;
            align-self: flex-end;
            border-bottom-right-radius: 0;
            background: #DCF8FF;
        }
        .timestamp {
            font-size: 10px;
            color: gray;
            text-align: right;
        }
        .chat-input {
            display: flex;
            padding: 10px;
            background: #f0f0f0;
            border-top: 1px solid #ccc;
        }
        input[type=text] {
            flex: 1;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        select, button {
            padding: 8px;
            margin-left: 5px;
            border: none;
            border-radius: 5px;
        }
        button {
            background: #128C7E;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background: #0b6b60;
        }
        .refresh-btn {
            background: #25D366;
            color: white;
        }
        .refresh-btn:hover {
            background: #1DA851;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">💬 Local Chat</div>

        <div class="chat-messages">
            {% for msg in messages %}
                <div class="message {{ msg['type'] }}">
                    <b>{{ msg['sender'] }}:</b> {{ msg['text'] }}<br>
                    <div class="timestamp">{{ msg['time'] }}</div>
                </div>
            {% endfor %}
        </div>

        <div class="chat-input">
            <form method="POST" action="/send" style="display:flex; width:100%;">
                <select name="sender">
                    <option value="You">You</option>
                    <option value="Friend">Friend</option>
                </select>
                <input type="text" name="message" placeholder="Type a message..." required>
                <button type="submit">Send</button>
                <button type="submit" formaction="/" class="refresh-btn">🔄</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, messages=messages)

@app.route("/send", methods=["POST"])
def send():
    sender = request.form.get("sender")
    text = request.form.get("message")
    now = datetime.datetime.now().strftime("%H:%M")
    msg_type = "receiver" if sender == "You" else "sender"
    messages.append({"sender": sender, "text": text, "time": now, "type": msg_type})
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
