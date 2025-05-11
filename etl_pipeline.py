# etl_pipeline.py
import pandas as pd

def extract_data():
    return pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 32, 29]
    })

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['age_plus_10'] = df['age'] + 10
    return df

def load_data(df: pd.DataFrame) -> str:
    # Simulates loading data — returns a CSV string
    return df.to_csv(index=False)


