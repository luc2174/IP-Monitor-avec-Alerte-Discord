import requests
import time
import json
import os

WEBHOOK_URL = "https://discord.com/api/webhooks/TON_WEBHOOK_ID/TON_TOKEN"
IP_FILE = "last_ip.txt"

def get_public_ip():
    try:
        return requests.get("https://api.ipify.org").text.strip()
    except Exception as e:
        print(f"Erreur pour obtenir l'IP : {e}")
        return None

def send_ip_to_discord(ip):
    data = {
        "content": f"@everyone 🌐 Nouvelle IP publique détectée : `{ip}`"
    }
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print("✅ IP envoyée à Discord.")
        else:
            print(f"❌ Erreur lors de l'envoi à Discord : {response.status_code}")
    except Exception as e:
        print(f"Erreur lors de l'envoi du webhook : {e}")

def read_last_ip():
    if os.path.exists(IP_FILE):
        with open(IP_FILE, "r") as f:
            return f.read().strip()
    return ""

def save_current_ip(ip):
    with open(IP_FILE, "w") as f:
        f.write(ip)

def main():
    while True:
        current_ip = get_public_ip()
        if current_ip:
            last_ip = read_last_ip()
            if current_ip != last_ip:
                print(f"🔁 IP changée : {last_ip} → {current_ip}")
                send_ip_to_discord(current_ip)
                save_current_ip(current_ip)
            else:
                print(f"🟢 IP inchangée : {current_ip}")
        time.sleep(60)

if __name__ == "__main__":
    main()

