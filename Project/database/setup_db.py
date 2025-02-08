from pymongo import MongoClient

# Connect to MongoDB
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)
db = client["summarizerDB"]
users_collection = db["users"]

print("MongoDB Connected! Database: summarizerDB")
