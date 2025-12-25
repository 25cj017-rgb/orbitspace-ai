from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

# ---------------------------------
# App initialization
# ---------------------------------
app = FastAPI(title="OrbitSpace AI – Space Debris Risk Analyzer")

# ---------------------------------
# CORS (frontend ↔ backend)
# ---------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------
# Serve frontend (STATIC FILES)
# ---------------------------------
# Folder structure:
# Backend/
# ├── main.py
# ├── static/
# │   ├── index.html
# │   ├── style.css
# │   └── script.js
# ---------------------------------

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

# ---------------------------------
# Request schema
# ---------------------------------
class PredictRequest(BaseModel):
    velocity: float   # km/s
    altitude: float   # km
    size: float       # cm
    density: float    # g/cm^3

# ---------------------------------
# Prediction API
# ---------------------------------
@app.post("/predict")
def predict_risk(data: PredictRequest):

    v = data.velocity
    h = data.altitude
    s = data.size
    d = data.density

    # Physics-based logic
    if v > 8.0 or h < 300 or s > 10:
        physics_risk = "High"
    elif v > 7.0 or s > 7:
        physics_risk = "Medium"
    else:
        physics_risk = "Low"

    # ML placeholder (safe)
    ml_risk = physics_risk

    # AI explanation
    if physics_risk == "High":
        insight = (
            "High collision risk detected due to unsafe orbital parameters. "
            "Immediate monitoring or mitigation is recommended."
        )
    elif physics_risk == "Medium":
        insight = (
            "Moderate collision risk observed. "
            "Close monitoring is advised."
        )
    else:
        insight = (
            "Low collision risk detected. "
            "Current orbital parameters are stable."
        )

    return {
        "physics_based_risk": physics_risk,
        "ml_predicted_risk": ml_risk,
        "ai_insight": insight
    }
