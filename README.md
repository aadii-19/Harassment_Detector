# Harassment Detector

## Overview
An AI-powered tool to detect harassment on **social media** and **workplace chats**.

## Features
- **Real-time monitoring** on web platforms.
- **AI-based detection** using ML .
- **Admin alerts** via Slack and Gmail SMTP.
- **Chrome extension** for seamless integration.

## Setup
1. **Clone Repository:**  
   ```
   git clone https://github.com/your-repo/harassment-detector.git
   cd harassment-detector
   ```
2. **Install Dependencies & Run Server:**  
```
pip install -r requirements.txt
uvicorn app:app --reload
```

3. **Load Chrome Extension:**
* Open chrome://extensions/
* Enable Developer Mode → Load Unpacked → Select extension/
* Set Up Gmail SMTP & Slack Webhook in app.py.

# POC:-
## Extension
![image](https://github.com/user-attachments/assets/dab828c8-a32f-4b2b-804a-f9033ff52944)

## O/P in Socialmedia
![image](https://github.com/user-attachments/assets/6492aadd-dac8-4ef9-b893-e09183967e1b)


## O/P in terminal
![image](https://github.com/user-attachments/assets/e5cccfdc-7176-404f-96e5-204ede6ea96d)

## Usage
The extension detects harassment, alerts users, and notifies admins via Slack and email.

