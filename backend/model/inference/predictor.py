import numpy as np
import pandas as pd

from artifacts.serializer import load_artifacts
from config.settings import FEATURE_COLS

def _build_feature_frame(input_data: dict) -> pd.DataFrame:
    """
    Validate incoming payload and build a single-row feature Dataframe
    in the exact training feature order.
    """
    missing = [col for col in FEATURE_COLS if col not in input_data]
    if missing:
        raise ValueError(f"Missing required features: {missing}")
    
    #keep only model features and enforce training order
    row = {col: input_data[col] for col in FEATURE_COLS}
    return pd.DataFrame([row], columns=FEATURE_COLS)

def predict_landslide(input_data: dict, threshold: float = 0.5) -> dict:
    """
    Run inference using saved best model + scaler.
    """
    model_name, model, scaler = load_artifacts()

    X = _build_feature_frame(input_data)
    X_for_scaler = X if hasattr(scaler, "feature_names_in_") else X.to_numpy()
    X_scaled = scaler.transform(X_for_scaler)

    # Works for sklearn models and your custom NeuralNetwork
    if hasattr(model, "predict_proba"):
        proba_raw = model.predict_proba(X_scaled)
        proba = float(np.ravel(proba_raw)[-1] if np.ndim(proba_raw) > 1 else np.ravel(proba_raw)[0])
        if np.ndim(proba_raw) > 1 and proba_raw.shape[1] >= 2:
            proba = float(proba_raw[0, 1])

    else:
        #fallback if model has only predict() fucntion
        pred = int(np.ravel(model.predict(X_scaled))[0])
        proba = float(pred)

    pred_class = int(proba >= threshold)

    return {
        "model_name": model_name,
        "prediction": pred_class,
        "label": "Landslide" if pred_class == 1 else "No Landslide",
        "probability_landslide": round(proba, 4),
        "confidence": round(proba if pred_class == 1 else (1 - proba), 4),
        "threshold": threshold,
    }