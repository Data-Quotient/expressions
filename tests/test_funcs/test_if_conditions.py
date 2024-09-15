import pytest
import pandas as pd  # For CSV creation
from main import run_parser, execute_datafusion_expr
from eval.evaluator import ast_to_datafusion_expr

@pytest.fixture
def csv_file(tmpdir):
    """Fixture to create a temporary CSV file with salary and tax columns."""
    data = {
        'salary': [5000, 6000, 7000],  # Salary values for the test cases
        'tax': [500, 600, 700]         # Tax values for nested IF test cases
    }
    df = pd.DataFrame(data)
    csv_path = tmpdir.join("test_data.csv")
    df.to_csv(csv_path, index=False)
    return str(csv_path)

# Test for simple IF condition
def test_if_condition(csv_file):
    """Test a simple IF condition: if salary > 6000, return 'High', else 'Low'."""
    input_expr = 'IF(GT("salary", 6000), \'High\', \'Low\')'
    expected_values = ["Low", "Low", "High"]  # Expected based on salary values

    ast = run_parser(input_expr)
    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)

    actual_values = result[0].to_pydict()['if']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"

# Test for IF-ELSE condition
def test_if_else_condition(csv_file):
    """Test an IF-ELSE condition: if salary > 6500, return 'High', else 'Low'."""
    input_expr = 'IF(GT("salary", 6500), \'High\', \'Low\')'
    expected_values = ["Low", "Low", "High"]  # Expected based on salary values

    ast = run_parser(input_expr)
    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)

    actual_values = result[0].to_pydict()['if']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"

# Test for nested IF-ELSEIF-ELSE condition
def test_if_elseif_else_condition(csv_file):
    """Test nested IF-ELSEIF-ELSE condition."""
    input_expr = 'IF(GT("salary", 6500), \'Very High\', IF(GTE("salary", 6000), \'High\', \'Low\'))'
    expected_values = ["Low", "High", "Very High"]

    ast = run_parser(input_expr)
    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)

    actual_values = result[0].to_pydict()['if']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"

# Test for IF condition where no condition is met
def test_if_no_condition_met(csv_file):
    """Test IF condition where no salary is greater than 8000, return 'Low'."""
    input_expr = 'IF(GT("salary", 8000), \'High\', \'Low\')'
    expected_values = ["Low", "Low", "Low"]  # None of the salaries exceed 8000

    ast = run_parser(input_expr)
    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)

    actual_values = result[0].to_pydict()['if']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"

# Test for nested IF condition with multiple layers
def test_nested_if_conditions(csv_file):
    """Test nested IF condition: if salary > 6500 and tax >= 700, return 'Very High'."""
    input_expr = 'IF(GT("salary", 6500), IF(GTE("tax", 700), \'Very High\', \'High\'), \'Low\')'
    expected_values = ["Low", "Low", "Very High"]  # Based on salary and tax values

    ast = run_parser(input_expr)
    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)

    actual_values = result[0].to_pydict()['if']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"
