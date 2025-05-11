import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a new column 'age_plus_10' to the DataFrame by adding 10 to the 'age' column.

    Parameters:
    df (pd.DataFrame): Input DataFrame with an 'age' column.

    Returns:
    pd.DataFrame: Transformed DataFrame with 'age_plus_10' column added.
    """
    df = df.copy()  # avoid modifying original
    df['age_plus_10'] = df['age'] + 10
    return df
