from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # 環境変数からトークンを取得
WEBHOOK_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

@app.route("/", methods=["GET"])
def home():
    return "Hello, Shinji! Your Telegram Bot Webhook is live!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    chat_id = data["message"]["chat"]["id"]
    message_text = data["message"]["text"]

    response_text = f"シンジ、受信しました: {message_text}"

    requests.post(WEBHOOK_URL, json={"chat_id": chat_id, "text": response_text})

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
