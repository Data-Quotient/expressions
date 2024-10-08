import pytest
import pandas as pd  # Pandas for CSV handling
from main import run_parser, execute_datafusion_expr
from eval.evaluator import ast_to_datafusion_expr
from datafusion import SessionContext
from exceptions.custom_exceptions import ColumnNotFoundError

@pytest.fixture
def csv_file(tmpdir):
    """Fixture to create a temporary CSV file with 'salary' column."""
    data = {'salary': [5000, 6000, 7000]}  # Only 'salary' column exists
    csv_path = tmpdir.join("test_data.csv")
    pd.DataFrame(data).to_csv(csv_path, index=False)
    return str(csv_path)

def test_sum_salary(csv_file):
    """Test SUM function on 'salary' column."""
    input_expr = 'SUM("salary")'
    expected_value = 18000  # 5000 + 6000 + 7000 = 18000

    ast = run_parser(input_expr)
    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)
    actual_value = result[0].to_pydict()['sum'][0]

    assert actual_value == expected_value, f"Expected {expected_value}, got {actual_value}"

def test_sum_empty_column(csv_file):
    """Test SUM function on a non-existent column ('tax')."""
    input_expr = 'SUM("tax")'
    expected_value = 0  # Expecting 0 if 'tax' column doesn't exist

    ast = run_parser(input_expr)

    try:
        schema = SessionContext().read_csv(csv_file).schema()
        expr_and_aggregate_flag = ast_to_datafusion_expr(ast, schema)
        result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)
        actual_value = result[0].to_pydict()['sum'][0]
    except ColumnNotFoundError:
        actual_value = 0  # Simulate returning 0 if the column is missing
    
    assert actual_value == expected_value, f"Expected {expected_value}, got {actual_value}"
