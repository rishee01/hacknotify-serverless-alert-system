# HackNotify Serverless Alert System

A serverless notification system built using AWS to automatically send opportunity alerts to a Telegram bot.

## Architecture

EventBridge → Lambda → DynamoDB → Telegram Bot

## AWS Services Used

- AWS Lambda
- Amazon EventBridge
- Amazon DynamoDB

## Features

- Automated alerts
- Serverless architecture
- Duplicate prevention using DynamoDB

## How It Works

1. EventBridge triggers Lambda
2. Lambda processes opportunity data
3. DynamoDB stores events
4. Telegram bot sends notifications
