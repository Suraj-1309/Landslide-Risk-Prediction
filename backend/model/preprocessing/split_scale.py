import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from config.settings import FEATURE_COLS


def split_and_scale(df_noisy: pd.DataFrame):
    """
    1. select features/target
    2. Train-test split
    3. Fit scaler on train, transform train/test
    """

    x = df_noisy[FEATURE_COLS]
    y = df_noisy["Landslide"]

    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, stratify=y, random_state=42
    )

    scaler =  StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test, X_train_s, X_test_s, scaler
