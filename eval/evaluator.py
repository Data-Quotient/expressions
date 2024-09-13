# eval/evaluator.py

from datafusion import functions as f, col, literal
from functools import reduce

# Function registry mapping function names to (function, is_aggregate) tuples
FUNCTION_REGISTRY = {
    'sum': (lambda args: f.sum(args[0]).alias('sum'), True),
    'subtract': (lambda args: (args[0] - args[1]).alias('subtract'), False),
    'add': (lambda args: (args[0] + args[1]).alias('add'), False),
    'multiply': (lambda args: (args[0] * args[1]).alias('multiply'), False),
    'divide': (lambda args: (args[0] / args[1]).alias('divide'), False),
    'if': (lambda args: f.when(args[0], args[1]).otherwise(args[2]).alias('if'), False),
    'and': (lambda args: reduce(lambda x, y: x & y, args).alias('and'), False),
    'gt': (lambda args: (args[0] > args[1]), False),
    'lt': (lambda args: (args[0] < args[1]), False),
    # Add other functions as needed
}

def ast_to_datafusion_expr(ast):
    """
    Convert the parsed AST into a DataFusion expression.
    This function recursively handles nested expressions.
    Returns a tuple: (expression, is_aggregate)
    """
    if isinstance(ast, int):
        return literal(ast), False  # Literal number is not an aggregate

    if isinstance(ast, str):
        return literal(ast), False  # Literal string is not an aggregate

    node_type = ast[0]

    if node_type == 'column':
        # Return a column expression
        column_name = ast[1]
        return col(column_name), False  # Column reference is not an aggregate

    elif node_type in FUNCTION_REGISTRY:
        # Recursively resolve the arguments to handle nested functions
        args = []
        is_aggregate = False
        for arg in ast[1]:
            expr, agg = ast_to_datafusion_expr(arg)
            args.append(expr)
            if agg:
                is_aggregate = True  # If any argument is an aggregate, set is_aggregate to True

        func, func_is_aggregate = FUNCTION_REGISTRY[node_type]
        expr = func(args)
        # The expression is aggregate if the function is aggregate
        is_aggregate = func_is_aggregate or is_aggregate
        return expr, is_aggregate
    else:
        raise ValueError(f"Unknown AST node {node_type}")
