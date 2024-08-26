import requests
import random
import time

# Read tokens from tokens.txt
with open("tokens.txt", "r") as file:
    tokens = file.read().splitlines()

# Read messages from messages.txt
with open("messages.txt", "r") as file:
    messages = file.read().splitlines()

# Specify the channel ID where messages will be sent
channel_id = "1258915876657434657"  # Replace with your channel ID

# Set headers template
headers_template = {
    "authority": "discord.com",
    "accept": "*/*",
    "accept-language": "en-US",
    "connection": "keep-alive",
    "content-type": "application/json",
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/@me",
    "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9015 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "en-US",
    "x-discord-timezone": "America/New_York",
}

# Function to send messages
def send_random_message():
    for token in tokens:
        headers = headers_template.copy()
        headers["Authorization"] = token

        message = random.choice(messages)  # Select a random message
        message_payload = {
            "content": message
        }
        requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=message_payload)
        time.sleep(5)  # Wait for 10 seconds before sending the next message

while True:
    send_random_message()
