import requests
import os
import time

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    r = requests.post(url, data=payload)
    print("Mesaj gönderildi:", r.status_code, r.text)

if _name_ == "_main_":
    while True:
        send_message("✅ Bot çalışıyor! Bu bir test mesajıdır.")
        time.sleep(3600)  # 1 saatte bir tekrar etsin
