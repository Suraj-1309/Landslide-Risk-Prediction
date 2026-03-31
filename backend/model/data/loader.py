import pandas as pd
from config.settings import DATASET_PATH, DATASET_COLS


def load_dataset() -> pd.DataFrame:
    """Load raw dataset with enforced schema."""
    return pd.read_csv(
        DATASET_PATH,
        header=0,
        names=DATASET_COLS,
        usecols=range(10)
    )