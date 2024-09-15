import pytest
import pandas as pd

@pytest.fixture
def csv_file(tmpdir):
    """Fixture to create a temporary CSV file with test data."""
    data = {
        'salary': [5000, 6000, 7000],
        'tax': [500, 600, 700],
        'bonus': [500, 600, 700],
    }
    df = pd.DataFrame(data)
    csv_path = tmpdir.join("test_data.csv")
    df.to_csv(csv_path, index=False)
    return str(csv_path)
