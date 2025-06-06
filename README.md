# AI Ticket Classifier with OpenAI + n8n

This is an automated support ticket classification system built using **OpenAI GPT-4o Mini** and **n8n**.

## Overview

The workflow receives a support message, classifies it into a category (billing, technical, feedback), detects urgency, and automatically replies if the issue is urgent — all without writing backend code.

## How It Works

1. A user message is sent via webhook.
2. An AI Agent classifies the message into a category and urgency using GPT.
3. If the urgency is high, another AI Agent generates a helpful response.
4. The response is sent to the user via Gmail.

## Key Features

- Classifies support tickets using AI
- Detects urgency levels
- Sends automated responses for urgent messages
- Fully built using no-code n8n workflow with OpenAI integration
