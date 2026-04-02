<p align="center">
  <img src="https://img.shields.io/badge/AWS-Lambda%20%7C%20DynamoDB-orange?style=for-the-badge&labelColor=111111">
  <img src="https://img.shields.io/badge/Python-Serverless-blue?style=for-the-badge&labelColor=000000">
  <img src="https://img.shields.io/badge/Telegram-Bot%20Alerts-26A5E4?style=for-the-badge&labelColor=000000">
  <img src="https://img.shields.io/badge/license-MIT-444444?style=for-the-badge&labelColor=000000">
</p>

<h1 align="center">🚀 HackNotify India</h1>

<p align="center">
Serverless automation system that sends <b>hackathon, internship, and tech event alerts</b> directly to Telegram using AWS Lambda.
</p>

<p align="center">
⚡ Automation • ☁️ Serverless • 🤖 Telegram Notifications
</p>

---

# 🧠 Overview

HackNotify India is a **serverless alert system** designed to automatically send **hackathon, internship, and tech opportunity notifications**.

The system uses **AWS Lambda + DynamoDB** to process events while preventing duplicate alerts.

It demonstrates a real-world **event-driven cloud architecture** used in production automation systems.

---

# ⚡ Features

| Feature                    | Description                                       |
| -------------------------- | ------------------------------------------------- |
| ☁️ Serverless Architecture | Runs entirely on AWS Lambda                       |
| 🚫 Duplicate Prevention    | DynamoDB stores events to prevent repeated alerts |
| 🤖 Telegram Integration    | Sends instant notifications                       |
| 📈 Scalable Design         | Can scale to thousands of events                  |
| ⏰ Automated Scheduling     | Can run automatically using EventBridge           |
| 🪶 Lightweight             | Python-based minimal system                       |

---

# 🏗 Architecture

```
Event Source
     │
     ▼
AWS Lambda Function
     │
     ▼
Check DynamoDB
     │
 ┌──Yes─── Duplicate → Ignore
 │
 No
 │
 ▼
Store Event in DynamoDB
 │
 ▼
Send Telegram Notification
```

### Components

| Service            | Purpose               |
| ------------------ | --------------------- |
| AWS Lambda         | Runs automation logic |
| Amazon DynamoDB    | Stores alert history  |
| Telegram Bot API   | Sends notifications   |
| Amazon EventBridge | Scheduler trigger     |

---

# 📦 Tech Stack

* Python
* AWS Lambda
* Amazon DynamoDB
* Telegram Bot API
* Boto3 (AWS SDK for Python)

---

# ⚙️ How It Works

1️⃣ Lambda function runs when triggered

2️⃣ System checks DynamoDB for existing event

3️⃣ If event **already exists → ignore**

4️⃣ If event **new → store event in DynamoDB**

5️⃣ Telegram bot sends notification

---

# 📢 Example Alert

🚀 **AWS Summit Bengaluru 2026**

One of the biggest cloud events bringing together developers, builders, and tech leaders exploring the future of **AI and cloud systems**.

📅 April 22–23, 2026
📍 KTPO Exhibition Center, Whitefield, Bengaluru

Two editions available:

**Innovators Edition – April 22**

For business leaders exploring AI & cloud transformation.

**Technical Edition – April 23**

For developers diving deep into AWS technologies.

---

Follow HackNotify India for:

• Hackathons

• Internships

• Tech events

• Certifications

• Job opportunities

🔗 https://bit.ly/HackNotify

---

# 🛠 Installation

### Clone repository

```bash
git clone https://github.com/rishee01/hacknotify-serverless-alert-system.git
```

### Move into project

```bash
cd hacknotify-serverless-alert-system
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Set these variables before running:

```env
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
TABLE_NAME=HackNotifyEvents
```

---

# ▶️ Run Locally

```bash
python lambda_function.py
```

---

# ☁️ Deploy to AWS

1️⃣ Create AWS Lambda function

2️⃣ Upload `lambda_function.py`

3️⃣ Attach IAM permissions for DynamoDB

4️⃣ Add environment variables

5️⃣ Trigger manually or using **EventBridge Scheduler**

---

# 🚀 Future Improvements

Planned upgrades for HackNotify:

* Devpost hackathon scraper
* Internship alerts
* Slack notifications
* Email alerts
* Multi-channel alerts
* Web dashboard for opportunities
* AI-powered opportunity ranking

---

# 📊 Project Stats

<p align="center">

<img src="https://github-readme-stats.vercel.app/api?username=rishee01&show_icons=true&theme=tokyonight">

<img src="https://github-readme-streak-stats.herokuapp.com/?user=rishee01&theme=tokyonight">

</p>

---

# 📜 License

MIT License — free to use and modify.

---

# 👨‍💻 Author

**Maharishee ambati**

Exploring: 

☁️ Cloud Automation

⚡ Serverless Systems

🤖 AI Engineering

---

<p align="center">

⭐ Star this repository if you found it useful

</p>
