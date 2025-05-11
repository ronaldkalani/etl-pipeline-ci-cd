import pandas as pd
from etl_pipeline import transform_data

def test_transform_data_validity():
    df = pd.DataFrame({'name': ['Test'], 'age': [30]})
    result = transform_data(df)
    
    assert 'age_plus_10' in result.columns
    assert result['age_plus_10'].iloc[0] == 40
