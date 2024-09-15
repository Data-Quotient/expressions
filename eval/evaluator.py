# eval/evaluator.py

from datafusion import functions as f, col, lit
from datafusion.functions import case
from functools import reduce
from exceptions.custom_exceptions import (
    DataTypeMismatchError,
    ColumnNotFoundError,
    InvalidOperationError,
)

# Function registry mapping function names to functions and is_aggregate flag
FUNCTION_REGISTRY = {
    'sum': (lambda arg: f.sum(arg).alias('sum'), True),
    'subtract': (lambda left, right: (left - right).alias('subtract'), False),
    'add': (lambda left, right: (left + right).alias('add'), False),
    'multiply': (lambda left, right: (left * right).alias('multiply'), False),
    'divide': (lambda left, right: (left / right).alias('divide'), False),
    'if': (lambda condition, true_expr, false_expr: case(condition)
           .when(lit(True), true_expr)
           .otherwise(false_expr)
           .alias('if'), False),
    'and': (lambda *conditions: reduce(lambda x, y: x & y, conditions).alias('and'), False),
    'gt': (lambda left, right: (left > right).alias('gt'), False),
    'gte': (lambda left, right: (left >= right).alias('gte'), False),
    'lt': (lambda left, right: (left < right).alias('lt'), False),
    'lte': (lambda left, right: (left <= right).alias('lte'), False),
    # Add other functions as needed
}

def ast_to_datafusion_expr(ast, df_schema=None):
    """Convert AST to DataFusion expression."""
    if isinstance(ast, int):
        return lit(ast), False  # Literal number is not an aggregate

    if isinstance(ast, str):
        return lit(ast), False  # Literal string is not an aggregate

    if isinstance(ast, tuple):
        node_type = ast[0]

        if node_type == 'column':
            column_name = ast[1]
            if df_schema and column_name not in df_schema:
                raise ColumnNotFoundError(column_name)
            return col(column_name), False  # Column reference is not an aggregate

        elif node_type == 'string':
            return lit(ast[1]), False  # String literal

        elif node_type in FUNCTION_REGISTRY:
            args = []
            is_aggregate = False
            for arg in ast[1]:
                expr, agg = ast_to_datafusion_expr(arg, df_schema)
                args.append(expr)
                if agg:
                    is_aggregate = True

            func, func_is_aggregate = FUNCTION_REGISTRY[node_type]
            expr = func(*args)  # Unpack args when calling the function
            is_aggregate = func_is_aggregate or is_aggregate
            return expr, is_aggregate
        else:
            raise InvalidOperationError(node_type, "Unknown AST node type")
    else:
        raise InvalidOperationError(str(ast), "Invalid AST node")
