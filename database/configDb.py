from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://divya:Letmesucceedsoon@customer-feedback.3qssb7i.mongodb.net/?retryWrites=true&w=majority&appName=customer-feedback"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.customer_feedback
try:
    client.server_info()
except Exception as e:
    print("MongoDB connection failed:", e)
    raise
products_collection = db["products"]
feedback_collection = db["feedback"]