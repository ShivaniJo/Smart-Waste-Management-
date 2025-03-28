from motor.motor_asyncio import AsyncIOMotorClient
from database import database

MONGO_URI = "mongodb+srv://shivanijoisar:<db_password>@cluster1.jcxq6os.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1c"
DB_NAME = "Cluster1"

print("Connected to MongoDB:", database.name)
client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
bins_collection = database["waste_bins"]  # Collection for storing bin data
from motor.motor_asyncio import AsyncIOMotorClient

