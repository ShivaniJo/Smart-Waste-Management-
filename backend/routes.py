from fastapi import APIRouter, HTTPException
from models import WasteBin
from database import bins_collection
from bson import ObjectId
from datetime import datetime

router = APIRouter()

# Add new waste bin data
@router.post("/bins/")
async def add_bin(bin_data: WasteBin):
    bin_dict = bin_data.dict()
    bin_dict["last_updated"] = datetime.utcnow()
    new_bin = await bins_collection.insert_one(bin_dict)
    return {"message": "Bin added successfully", "id": str(new_bin.inserted_id)}

# Get all waste bins
@router.get("/bins/")
async def get_all_bins():
    bins = await bins_collection.find().to_list(100)
    for bin in bins:
        bin["_id"] = str(bin["_id"])  # Convert ObjectId to string
    return bins

# Get bin by ID
@router.get("/bins/{bin_id}")
async def get_bin(bin_id: str):
    bin = await bins_collection.find_one({"_id": ObjectId(bin_id)})
    if bin:
        bin["_id"] = str(bin["_id"])
        return bin
    raise HTTPException(status_code=404, detail="Bin not found")

# Update bin fill level
@router.put("/bins/{bin_id}")
async def update_bin(bin_id: str, current_fill: float):
    update_result = await bins_collection.update_one(
        {"_id": ObjectId(bin_id)},
        {"$set": {"current_fill": current_fill, "last_updated": datetime.utcnow()}}
    )
    if update_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Bin not found or no changes made")
    return {"message": "Bin updated successfully"}

# Delete bin
@router.delete("/bins/{bin_id}")
async def delete_bin(bin_id: str):
    delete_result = await bins_collection.delete_one({"_id": ObjectId(bin_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Bin not found")
    return {"message": "Bin deleted successfully"}
