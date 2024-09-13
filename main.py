import pyarrow as pa
from datafusion import SessionContext
from core.lexer import lexer
from core.parser import parser
from eval.evaluator import ast_to_datafusion_expr  # Import the evaluator

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

def execute_datafusion_expr(expr_and_aggregate_flag, csv_path):
    """ Execute a DataFusion expression on a CSV file and return the result. """
    expr, is_aggregate = expr_and_aggregate_flag
    ctx = SessionContext()

    # Register the CSV file as a table
    ctx.register_csv("table", csv_path)

    # Build the query with the DataFusion expression
    df = ctx.table("table")

    if is_aggregate:
        # Use aggregate method
        df_result = df.aggregate([], [expr])
    else:
        # Use select method
        df_result = df.select(expr)

    # Collect the result and catch errors
    try:
        result = df_result.collect()
        print("DataFusion Result:", result)
        return result
    except Exception as e:
        print(f"DataFusion Execution Failed: {e}")
        raise