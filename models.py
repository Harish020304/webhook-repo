
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

MONGO_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGO_URI)
db = client.github_events
collection = db.events

def insert_event(event_data):
    collection.insert_one(event_data)

def get_latest_events():
    events = collection.find().sort("timestamp", -1).limit(10)
    result = []
    for event in events:
        event["_id"] = str(event["_id"])  # Fix ObjectId
        event["timestamp"] = event["timestamp"].strftime("%d %B %Y - %I:%M %p UTC")
        result.append(event)
    return result
