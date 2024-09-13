import pytest
from main import run_lexer, run_parser, execute_datafusion_expr
from evaluator import ast_to_datafusion_expr
import pandas as pd

@pytest.fixture
def sample_input_expr():
    """ Fixture to provide a sample input expression """
    return 'SUBTRACT("salary", "tax")'

@pytest.fixture
def csv_file(tmpdir):
    """ Fixture to create a temporary CSV file with test data """
    data = {
        'salary': [5000, 6000, 7000],
        'tax': [500, 600, 700]
    }
    df = pd.DataFrame(data)
    csv_path = tmpdir.join("test_data.csv")
    df.to_csv(csv_path, index=False)
    return str(csv_path)

def test_run_lexer(sample_input_expr):
    """ Test the lexer function """
    tokens = run_lexer(sample_input_expr)
    assert len(tokens) > 0  # Ensure tokens are generated
    assert tokens[0].type == "SUBTRACT"  # First token should be SUBTRACT
    assert tokens[2].value == "salary"  # Third token should be the salary column

def test_run_parser(sample_input_expr):
    """ Test the parser function """
    ast = run_parser(sample_input_expr)
    assert isinstance(ast, tuple)  # Ensure we get an AST tuple
    assert ast[0] == 'subtract'  # Check for correct operation
    assert ast[1][1] == "salary"  # First argument should be the salary column

def test_execute_datafusion_expr(sample_input_expr, csv_file):
    """ Test executing a DataFusion expression on a CSV """
    ast = run_parser(sample_input_expr)
    df_expr = ast_to_datafusion_expr(ast)
    result = execute_datafusion_expr(df_expr, csv_file)
    
    # Ensure the result is correct
    assert result is not None
    assert len(result) > 0  # Ensure we have results
    assert result[0].to_pydict()['subtract'][0] == 4500  # First row should be 5000 - 500 = 4500
