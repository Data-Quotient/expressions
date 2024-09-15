import pytest
from main import run_parser, execute_datafusion_expr
from eval.evaluator import ast_to_datafusion_expr
import pandas as pd

@pytest.fixture
def csv_file(tmpdir):
    """Fixture to create a temporary CSV file with salary and bonus data."""
    data = {
        'salary': [5000, 6000, 7000],
        'bonus': [500, 600, 700]
    }
    df = pd.DataFrame(data)
    csv_path = tmpdir.join("test_data.csv")
    df.to_csv(csv_path, index=False)
    return str(csv_path)

@pytest.fixture
def csv_file_no_bonus(tmpdir):
    """Fixture to create a temporary CSV file without the bonus column."""
    data = {
        'salary': [5000, 6000, 7000]
    }
    df = pd.DataFrame(data)
    csv_path = tmpdir.join("test_data_no_bonus.csv")
    df.to_csv(csv_path, index=False)
    return str(csv_path)

def test_add_salary_bonus(csv_file):
    """Test ADD function with salary and bonus columns."""
    input_expr = 'ADD("salary", "bonus")'
    expected_values = [5500, 6600, 7700]

    ast = run_parser(input_expr)
    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)

    actual_values = result[0].to_pydict()['add']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"

def test_add_no_bonus(csv_file_no_bonus):
    """Test ADD function with salary only and no bonus column."""
    input_expr = 'ADD("salary", 0)'  # Handle missing bonus by adding 0
    expected_values = [5000, 6000, 7000]

    ast = run_parser(input_expr)
    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file_no_bonus)

    actual_values = result[0].to_pydict()['add']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"
