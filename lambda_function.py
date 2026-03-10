import json
import urllib.request
import boto3
import datetime
import os

# -----------------------------
# Configuration
# -----------------------------

BOT_TOKEN = "8766545056:AAHGBMAh10YhUzakM-oyNJJSc9HSIcNzM9Y"
CHAT_ID = "1112321920"

TABLE_NAME = "HackNotifyEvents"

# -----------------------------
# DynamoDB Setup
# -----------------------------

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)

# -----------------------------
# Telegram Sender
# -----------------------------

def send_telegram_message(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = json.dumps({
        "chat_id": CHAT_ID,
        "text": message
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"}
    )

    try:
        response = urllib.request.urlopen(req)
        result = response.read().decode()
        print("Telegram response:", result)

    except Exception as e:
        print("Telegram error:", e)

# -----------------------------
# DynamoDB Helpers
# -----------------------------

def event_exists(event_id):

    try:
        response = table.get_item(Key={"event_id": event_id})
        return "Item" in response

    except Exception as e:
        print("DynamoDB error:", e)
        return False


def store_event(event_id, title):

    try:
        table.put_item(
            Item={
                "event_id": event_id,
                "title": title,
                "timestamp": str(datetime.datetime.utcnow())
            }
        )

    except Exception as e:
        print("DynamoDB store error:", e)

# -----------------------------
# Main Lambda Function
# -----------------------------

def lambda_handler(event, context):

    event_id = "hackathon_001"
    title = "AI Global Hackathon 2026"

    print("Checking event:", event_id)

    if not event_exists(event_id):

        print("New event detected")

        store_event(event_id, title)

        message = f"""
🚀 HackNotify Alert

{title}

Stay tuned for more opportunities!
"""

        send_telegram_message(message)

        return {
            "statusCode": 200,
            "body": "New alert sent"
        }

    print("Event already exists")

    return {
        "statusCode": 200,
        "body": "Event already exists. No alert sent."
    }

# -----------------------------
# Local Test
# -----------------------------

if __name__ == "__main__":
    lambda_handler({}, None)