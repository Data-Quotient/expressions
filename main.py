import pyarrow as pa
from datafusion import SessionContext
from parser.lexer import lexer
from parser.parser import parser
from evaluator import ast_to_datafusion_expr  # Import the evaluator

def run_lexer(input_string):
    """ Lex the input string and return the tokens. """
    lexer.input(input_string)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens

def run_parser(input_string):
    """ Parse the input string and return the AST. """
    result = parser.parse(input_string)
    return result

def execute_datafusion_expr(expr, csv_path):
    """ Execute a DataFusion expression on a CSV file and return the result. """
    ctx = SessionContext()

    # Register the CSV file as a table
    ctx.register_csv("table", csv_path)
    
    # Build the query with the DataFusion expression
    df_result = ctx.table("table").select(expr)
    
    # Collect the result
    result = df_result.collect()
    return result
