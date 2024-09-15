import pytest
import pandas as pd
from main import run_parser, execute_datafusion_expr
from eval.evaluator import ast_to_datafusion_expr

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

def test_sum_salary(csv_file):
    """Test the SUM function on the 'salary' column."""
    input_expr = 'SUM("salary")'
    expected_value = 18000  # Since sum of [5000, 6000, 7000] is 18000

    ast = run_parser(input_expr)
    print(f"Parsed AST for {input_expr}: {ast}")

    if ast is None:
        raise ValueError(f"Parser failed for input: {input_expr}")

    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    expr, is_aggregate = expr_and_aggregate_flag
    print(f"Generated DataFusion Expression: {expr}")
    print(f"Is Aggregate: {is_aggregate}")

    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)
    print(f"Execution Result: {result}")

    # Extract the aggregated sum value
    actual_value = result[0].to_pydict()['sum'][0]
    assert actual_value == expected_value, f"Expected {expected_value}, got {actual_value}"

def test_subtract_salary_tax(csv_file):
    """Test the SUBTRACT function on 'salary' and 'tax' columns."""
    input_expr = 'SUBTRACT("salary", "tax")'
    expected_values = [4500, 5400, 6300]

    ast = run_parser(input_expr)
    print(f"Parsed AST for {input_expr}: {ast}")

    if ast is None:
        raise ValueError(f"Parser failed for input: {input_expr}")

    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    expr, is_aggregate = expr_and_aggregate_flag
    print(f"Generated DataFusion Expression: {expr}")
    print(f"Is Aggregate: {is_aggregate}")

    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)
    print(f"Execution Result: {result}")

    actual_values = result[0].to_pydict()['subtract']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"

def test_add_salary_bonus(csv_file):
    """Test the ADD function on 'salary' and 'bonus' columns."""
    input_expr = 'ADD("salary", "bonus")'
    expected_values = [5500, 6600, 7700]

    ast = run_parser(input_expr)
    print(f"Parsed AST for {input_expr}: {ast}")

    if ast is None:
        raise ValueError(f"Parser failed for input: {input_expr}")

    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    expr, is_aggregate = expr_and_aggregate_flag
    print(f"Generated DataFusion Expression: {expr}")
    print(f"Is Aggregate: {is_aggregate}")

    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)
    print(f"Execution Result: {result}")

    actual_values = result[0].to_pydict()['add']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"


def test_and_condition(csv_file):
    """Test the AND function with two conditions."""
    input_expr = 'AND(GT("salary", 5500), LT("tax", 700))'
    expected_values = [False, True, False]  # Based on the data

    ast = run_parser(input_expr)
    print(f"Parsed AST for {input_expr}: {ast}")

    if ast is None:
        raise ValueError(f"Parser failed for input: {input_expr}")

    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    expr, is_aggregate = expr_and_aggregate_flag
    print(f"Generated DataFusion Expression: {expr}")
    print(f"Is Aggregate: {is_aggregate}")

    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)
    print(f"Execution Result: {result}")

    actual_values = result[0].to_pydict()['and']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"


def test_if_condition(csv_file):
    """Test the IF function with a simple condition."""
    input_expr = 'IF(GT("salary", 6000), \'High\', \'Low\')'
    expected_values = ["Low", "Low", "High"]  # Salaries are 5000, 6000, 7000

    ast = run_parser(input_expr)
    print(f"Parsed AST for {input_expr}: {ast}")

    if ast is None:
        raise ValueError(f"Parser failed for input: {input_expr}")

    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    expr, is_aggregate = expr_and_aggregate_flag
    print(f"Generated DataFusion Expression: {expr}")
    print(f"Is Aggregate: {is_aggregate}")

    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)
    print(f"Execution Result: {result}")

    actual_values = result[0].to_pydict()['if']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"
def test_nested_if_condition(csv_file):
    """Test nested IF functions with GTE."""
    input_expr = 'IF(GT("salary", 6500), \'Very High\', IF(GTE("salary", 6000), \'High\', \'Low\'))'
    expected_values = ["Low", "High", "Very High"]  # Salaries are 5000, 6000, 7000

    ast = run_parser(input_expr)
    print(f"Parsed AST for {input_expr}: {ast}")

    if ast is None:
        raise ValueError(f"Parser failed for input: {input_expr}")

    expr_and_aggregate_flag = ast_to_datafusion_expr(ast)
    expr, is_aggregate = expr_and_aggregate_flag
    print(f"Generated DataFusion Expression: {expr}")
    print(f"Is Aggregate: {is_aggregate}")

    result = execute_datafusion_expr(expr_and_aggregate_flag, csv_file)
    print(f"Execution Result: {result}")

    actual_values = result[0].to_pydict()['if']
    assert actual_values == expected_values, f"Expected {expected_values}, got {actual_values}"
