from fastapi import FastAPI
from routes import router as waste_router
from backend.route_optimization import router as route_optimization_router

app = FastAPI()

# Include waste bin routes
app.include_router(waste_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Smart Waste Management System API"}

