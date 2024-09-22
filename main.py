# main.py

import pyarrow as pa
from datafusion import SessionContext
from core.lexer import lexer
from core.parser import parser

def run_lexer(input_string):
    """Lex the input string and return the tokens."""
    lexer.input(input_string)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens

def run_parser(input_string):
    """Parse the input string and return the AST."""
    result = parser.parse(input_string)
    return result

def execute_datafusion_expr(expr_and_aggregate_flag, csv_file):
    """Execute the DataFusion expression on the CSV file"""
    ctx = SessionContext()
    df = ctx.read_csv(csv_file)  # Read the CSV into a DataFrame
    expr, is_aggregate = expr_and_aggregate_flag
    
    if is_aggregate:
        # Aggregate expressions should be used with the `aggregate` function
        result_df = df.aggregate([], [expr])
    else:
        # Regular expressions should be used with `select`
        result_df = df.select(expr)
        
    return result_df.collect()  # Return the result for verification 