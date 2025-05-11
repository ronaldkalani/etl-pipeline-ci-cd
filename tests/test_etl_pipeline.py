# tests/test_etl_pipeline.py
import pandas as pd
from etl_pipeline import extract_data, transform_data, load_data

def test_extract_data():
    df = extract_data()
    assert not df.empty
    assert list(df.columns) == ['name', 'age']
    assert df.shape == (3, 2)

def test_transform_data():
    df = pd.DataFrame({'name': ['Alice'], 'age': [30]})
    result = transform_data(df)
    assert 'age_plus_10' in result.columns
    assert result['age_plus_10'].iloc[0] == 40

def test_load_data():
    df = pd.DataFrame({'name': ['Alice'], 'age': [25], 'age_plus_10': [35]})
    result = load_data(df)
    assert isinstance(result, str)
    assert "Alice" in result
    assert "35" in result

