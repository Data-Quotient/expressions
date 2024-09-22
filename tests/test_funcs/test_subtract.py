import pytest
import pandas as pd
from main import run_parser, execute_datafusion_expr
from eval.evaluator import ast_to_datafusion_expr

@pytest.fixture
def csv_file(tmpdir):
    """Fixture to create a temporary CSV file with salary and tax columns."""
    data = {
        'salary': [5000, 6000, 7000],
        'tax': [500, 600, 700]
    }
    csv_path = tmpdir.join("test_data.csv")
    pd.DataFrame(data).to_csv(csv_path, index=False)
    return str(csv_path)

def run_test(input_expr, expected_values, csv_file, result_key='subtract'):
    """Helper function to run the expression and validate the result."""
    ast = run_parser(input_expr)
    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)
    actual_values = result[0].to_pydict()[result_key]
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"

def test_subtract_salary_tax(csv_file):
    """Test SUBTRACT function on 'salary' and 'tax' columns."""
    input_expr = 'SUBTRACT("salary", "tax")'
    expected_values = [4500, 5400, 6300]
    run_test(input_expr, expected_values, csv_file)

def test_subtract_empty_column(csv_file):
    """Test SUBTRACT function on 'salary' without the 'bonus' column, subtracting 0."""
    input_expr = 'SUBTRACT("salary", 0)'  # Handle missing bonus by subtracting 0
    expected_values = [5000, 6000, 7000]  # No bonus, so salary remains unchanged
    run_test(input_expr, expected_values, csv_file)
