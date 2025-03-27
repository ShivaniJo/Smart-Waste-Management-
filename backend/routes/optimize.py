from fastapi import APIRouter
import numpy as np
from sklearn.cluster import KMeans
from database import get_sensors  # Fetch sensor data

router = APIRouter()

@router.get("/optimize-routes")
def optimize_routes():
    sensors = get_sensors()
    
    # Extract locations of bins that are nearly full
    locations = np.array([
        (s["latitude"], s["longitude"])
        for s in sensors if s["current_fill"] / s["bin_capacity"] > 0.7  # Threshold for full bins
    ])
    
    if len(locations) == 0:
        return {"message": "No bins require urgent collection"}

    # Use KMeans clustering to group bins into collection routes
    num_clusters = min(len(locations), 5)  # Adjust based on capacity
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(locations)
    
    optimized_routes = [
        {"route": idx, "latitude": lat, "longitude": lon}
        for idx, (lat, lon) in zip(kmeans.labels_, locations)
    ]

    return {"routes": optimized_routes}
