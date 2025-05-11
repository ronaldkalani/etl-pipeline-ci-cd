import pandas as pd

def extract_data():
    # Simulate extracting raw data
    return pd.DataFrame({
        'name': ['Alice', 'Bob'],
        'age': [25, 32]
    })

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['age_plus_10'] = df['age'] + 10
    return df

def load_data(df: pd.DataFrame):
    # Simulate loading (e.g., to CSV)
    return df.to_csv(index=False)

