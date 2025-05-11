import pandas as pd

def extract_data():
    # Simulate data extraction
    return pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35]
    })

def transform_data(df):
    # Example transformation: add 10 years to age
    df['age_plus_10'] = df['age'] + 10
    return df

def load_data(df):
    # Simulate load by returning CSV string
    return df.to_csv(index=False)
