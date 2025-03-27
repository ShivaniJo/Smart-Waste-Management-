from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "waste_management"

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
bins_collection = database["waste_bins"]  # Collection for storing bin data
