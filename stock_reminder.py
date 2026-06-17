import yfinance as yf
import subprocess
import requests
import time
import os
import platform
import json

STOCKS = {
    "GEN": {"above": 26}
    }
CHECK_INTERVAL = 3600

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")

STATE_FILE = "alert_state.json"



def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def notify_mac(title, message):
    if platform.system() == "Darwin":
        script = f'display notification "{message}" with title "{title}" sound name "Ping"'
        subprocess.run(["osascript", "-e", script])

def notify_discord(message):
    if DISCORD_WEBHOOK_URL:
        requests.post(DISCORD_WEBHOOK_URL, json={"content": message})

def notify(title, message):
    notify_mac(title, message)
    notify_discord(f"**{title}** {message}")


def check_prices():
    state = load_state()

    for ticker, thresholds in STOCKS.items():
        try:
            stock = yf.Ticker(ticker)
            price = stock.fast_info["last_price"]
            print(f"{ticker}: ${price:.2f}")

            key_above = f"{ticker}_above"
            if thresholds.get("above"):
                if price > thresholds["above"]:
                    if not state.get(key_above):
                        notify(f"📈 {ticker} vysoko!", f"Cena ${price:.2f} je nad {thresholds['above']}")
                        state[key_above] = True
                else:
                    state[key_above] = False

        except Exception as e:
            print(f"Chyba u {ticker}: {e}")
    save_state(state)