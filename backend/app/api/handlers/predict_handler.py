from pathlib import Path
import pickle

import numpy as np
import pandas as pd

from app.api.schemas.data_schema import PredictRequest

BASE_DIR = Path(__file__).resolve().parents[3] #backend/
MODEL_PATH = BASE_DIR / "model" / "artifacts" / "best_model.pkl"
SCALER_PATH = BASE_DIR / "model" / "artifacts" / "scaler.pkl"

FEATURE_COLS = [
    "Rainfall_mm",
    "Slope_Angle",
    "Soil_Saturation",
    "Vegetation_Cover",
    "Earthquake_Activity",
    "Proximity_to_Water",
    "Soil_Type_Gravel",
    "Soil_Type_Sand",
    "Soil_Type_Silt",
]

def _load_artifacts():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    if not SCALER_PATH.exists():
        raise FileNotFoundError(f"Scaler file not found: {SCALER_PATH}")
    
    with open(MODEL_PATH, "rb") as f:
        model_payload = pickle.load(f)

    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)

    model = model_payload["model"] if isinstance(model_payload, dict) else model_payload
    return model, scaler

def _build_feature_frame(payload: PredictRequest) -> pd.DataFrame:
    row = {
        "Rainfall_mm": payload.rainfall_mm,
        "Slope_Angle": payload.slope_angle,
        "Soil_Saturation": payload.soil_saturation,
        "Vegetation_Cover": payload.vegetation_cover,
        "Earthquake_Activity": payload.earthquake_activity,
        "Proximity_to_Water": payload.proximity_to_water,
        "Soil_Type_Gravel": payload.soil_type_gravel,
        "Soil_Type_Sand": payload.soil_type_sand,
        "Soil_Type_Silt": payload.soil_type_silt,
    }
    return pd.DataFrame([row], columns=FEATURE_COLS)

def predict_landslide_service(payload: PredictRequest) -> dict:
    model, scaler = _load_artifacts()
    X = _build_feature_frame(payload)

    X_scaled = scaler.transform(X)

    if hasattr(model, "predict_proba"):
        proba_raw = model.predict_proba(X_scaled)
        if np.ndim(proba_raw) > 1 and proba_raw.shape[1] >= 2:
            probability = float(proba_raw[0, 1])
        else:
            probability = float(np.ravel(proba_raw)[0])
    else:
        pred = int(np.ravel(model.predict(X_scaled))[0])
        probability = float(pred)

    probability = max(0.0, min(1.0, probability))
    landslide = probability >= 0.5

    return {
        "landslide" : bool(landslide),
        "probability" : round(probability, 2),
    }