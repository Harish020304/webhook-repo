# 📡 GitHub Webhook Tracker

A full-stack application that listens to GitHub Webhook events (Push, Pull Request, Merge) and logs them into a MongoDB database. A frontend UI displays the latest activity by polling the backend every 15 seconds.

---

## 🚀 Features

- Receive GitHub webhook events: `push`, `pull_request`, and `merge` (inferred from PR merged).
- Store event details in MongoDB.
- Display the latest events on a frontend UI with live updates every 15 seconds.
- Clean, user-friendly event message format.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: MongoDB
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **Other**: Ngrok (for local webhook testing), Dotenv, 

---

## 📂 Project Structure
├── app.py               # Main Flask app
├── model.py                # MongoDB connection + DB helper functions
├── templates/
│   └── index.html       # UI for viewing events
├── static/
│   └── main.js          # JS for rendering
├── .env                 # Environment variables (ignored in Git)
├── .gitignore
├── requirements.txt
└── README.md


## 🚀 Getting Started
bash
git clone https://github.com/MadhukarMP-2002/webhook-repo-.git
cd webhook-repo
pip install -r requirements.txt
python server.py
Visit http://127.0.0.1:5000/ in your browser.
ngrok http 5000

# also u can add the deployed url if the project is deployed in cloud(render,aws,etc)

# GitHub Webhook Setup or Action-repo Setuo
1. Navigate to your GitHub repository Settings > Webhooks

2. Click Add webhook

3. Configure:

    -Payload URL: http://your-server-url/webhook (replace with your ngrok or deployed URL)

    -Content type: application/json

    -Which events: Select Just the push event or Send me everything