import pandas as pd
from etl_pipeline import transform_data

def test_transform_data_validity():
    df = pd.DataFrame({'col1': [1, 2]})
    result = transform_data(df)
    assert 'processed_col' in result.columns
    assert result['processed_col'].tolist() == [10, 20]
