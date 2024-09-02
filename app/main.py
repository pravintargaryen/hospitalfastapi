from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import Dict, List

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods, adjust as needed
    allow_headers=["*"],  # Allow all headers, adjust as needed
)

# Load the JSON data
with open("data.json", "r") as f:
    data = json.load(f)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Hospital API"}

# Emergency Endpoints
@app.get("/emergency/bed-availability", response_model=List[Dict])
def get_bed_availability():
    return data["emergency"]["bedAvailability"]

@app.get("/emergency/patient-queue", response_model=List[Dict])
def get_patient_queue():
    return data["emergency"]["patientQueue"]

@app.get("/emergency/staff-schedule", response_model=List[Dict])
def get_staff_schedule():
    return data["emergency"]["staffSchedule"]

@app.get("/emergency/ambulance-tracking", response_model=List[Dict])
def get_ambulance_tracking():
    return data["emergency"]["ambulanceTracking"]

# Blood Bank Endpoints
@app.get("/blood/inventory", response_model=Dict[str, int])
def get_blood_inventory():
    return data["bloodBank"]["bloodInventory"]

@app.get("/blood/donors", response_model=Dict[str, int])
def get_donors():
    return data["bloodBank"]["donors"]

@app.get("/blood/requests", response_model=List[Dict])
def get_requests():
    return data["bloodBank"]["requests"]

@app.get("/blood/donor-trends", response_model=List[Dict])
def get_donor_trends():
    return data["bloodBank"]["donorTrends"]

# Pharmacy Endpoints
@app.get("/pharmacy/stock-details", response_model=List[Dict])
def get_pharmacy_stock_details():
    return data["pharmacy"]["pharmacyStockDetails"]

@app.get("/pharmacy/order-details", response_model=List[Dict])
def get_order_details():
    return data["pharmacy"]["orderDetails"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
