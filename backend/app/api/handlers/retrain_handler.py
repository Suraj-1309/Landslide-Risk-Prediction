from pathlib import Path

import pandas as pd

from model.pipelines.retrain_pipeline import run_retraining_pipeline


BASE_DIR = Path(__file__).resolve().parents[3]  # backend/
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
LANDSLIDE_DATASET_PATH = RAW_DATA_DIR / "landslide_dataset.csv"
REQUEST_DATASET_PATH = RAW_DATA_DIR / "request_landslide_dataset.csv"

DATASET_COLS = [
    "Rainfall_mm",
    "Slope_Angle",
    "Soil_Saturation",
    "Vegetation_Cover",
    "Earthquake_Activity",
    "Proximity_to_Water",
    "Landslide",
    "Soil_Type_Gravel",
    "Soil_Type_Sand",
    "Soil_Type_Silt",
]

def _load_main_dataset() -> pd.DataFrame:
    if not LANDSLIDE_DATASET_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {LANDSLIDE_DATASET_PATH}")

    # The original file has a malformed header; force expected columns.
    return pd.read_csv(
        LANDSLIDE_DATASET_PATH,
        header=0,
        names=DATASET_COLS,
        usecols=range(10),
    )


def _load_request_dataset() -> pd.DataFrame:
    if not REQUEST_DATASET_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {REQUEST_DATASET_PATH}")

    df = pd.read_csv(REQUEST_DATASET_PATH)
    if set(DATASET_COLS).issubset(df.columns):
        return df[DATASET_COLS].copy()

    if df.shape[1] == len(DATASET_COLS):
        df.columns = DATASET_COLS
        return df

    raise ValueError(
        "request_landslide_dataset.csv does not match expected dataset schema"
    )


def retrain_model_service() -> dict:
    main_df = _load_main_dataset()
    request_df = _load_request_dataset()
    return run_retraining_pipeline(main_df, request_df)
