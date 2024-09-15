import pytest
import pandas as pd  # You need pandas for DataFrame manipulation
from main import run_parser, execute_datafusion_expr
from eval.evaluator import ast_to_datafusion_expr

@pytest.fixture
def csv_file(tmpdir):
    """Fixture to create a temporary CSV file with salary and tax columns."""
    data = {
        'salary': [5000, 6000, 7000],
        'tax': [500, 600, 700]
    }
    df = pd.DataFrame(data)
    csv_path = tmpdir.join("test_data.csv")
    df.to_csv(csv_path, index=False)
    return str(csv_path)

def test_subtract_salary_tax(csv_file):
    """Test SUBTRACT function on salary and tax columns."""
    input_expr = 'SUBTRACT("salary", "tax")'
    expected_values = [4500, 5400, 6300]

    # Parse and convert expression to datafusion expression
    ast = run_parser(input_expr)
    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)

    # Execute the expression on the CSV file
    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)

    # Extract the result and validate it
    actual_values = result[0].to_pydict()['subtract']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"

def test_subtract_empty_column(csv_file):
    """Test SUBTRACT function with salary but no bonus column."""
    input_expr = 'SUBTRACT("salary", 0)'  # Handle missing bonus by subtracting 0
    expected_values = [5000, 6000, 7000]  # No bonus, so salary remains unchanged

    # Parse and convert expression to datafusion expression
    ast = run_parser(input_expr)
    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)

    # Execute the expression on the CSV file
    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)

    # Extract the result and validate it
    actual_values = result[0].to_pydict()['subtract']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"
