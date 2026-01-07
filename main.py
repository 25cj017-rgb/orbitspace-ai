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

    # ---------------------------------
    # Physics-inspired risk scoring
    # ---------------------------------
    risk_score = 0

    # Velocity contribution
    if v >= 12:
        risk_score += 3
    elif v >= 8:
        risk_score += 2
    elif v >= 5:
        risk_score += 1

    # Debris size contribution
    if s >= 100:
        risk_score += 3
    elif s >= 50:
        risk_score += 2
    elif s >= 10:
        risk_score += 1

    # Altitude contribution (LEO congestion zone)
    if 300 <= h <= 1000:
        risk_score += 2
    elif h < 300:
        risk_score += 1

    # Density contribution
    if d >= 7:
        risk_score += 2
    elif d >= 3:
        risk_score += 1

    # ---------------------------------
    # Final risk classification
    # ---------------------------------
    if risk_score >= 8:
        physics_risk = "High"
    elif risk_score >= 4:
        physics_risk = "Medium"
    else:
        physics_risk = "Low"

    # ML prediction (proxy for demo)
    ml_risk = physics_risk

    # ---------------------------------
    # AI Insight
    # ---------------------------------
    if physics_risk == "High":
        insight = (
            "High collision risk detected due to high relative velocity, "
            "large debris size, dense material, and operation within a "
            "congested low Earth orbit region. Immediate mitigation is recommended."
        )
    elif physics_risk == "Medium":
        insight = (
            "Moderate collision risk observed. Certain orbital parameters "
            "indicate potential hazards, and continuous monitoring is advised."
        )
    else:
        insight = (
            "Low collision risk detected. The current orbital parameters "
            "indicate a stable and safe trajectory."
        )

    return {
        "physics_based_risk": physics_risk,
        "ml_predicted_risk": ml_risk,
        "risk_score": risk_score,
        "ai_insight": insight
    }
