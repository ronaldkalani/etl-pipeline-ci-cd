import pandas as pd

def transform_data(df):
    # Example transformation
    df['processed_col'] = df['col1'].apply(lambda x: x * 10)
    return df
