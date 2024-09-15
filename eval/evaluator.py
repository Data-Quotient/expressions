# eval/evaluator.py

from datafusion import functions as f, col, literal
from datafusion.functions import case
from functools import reduce
from exceptions.custom_exceptions import DataTypeMismatchError, ColumnNotFoundError, InvalidOperationError

# Function registry mapping function names to (function, is_aggregate) tuples
FUNCTION_REGISTRY = {
    'sum': (lambda args: f.sum(args[0]).alias('sum'), True),
    'subtract': (lambda args: (args[0] - args[1]).alias('subtract'), False),
    'add': (lambda args: (args[0] + args[1]).alias('add'), False),
    'multiply': (lambda args: (args[0] * args[1]).alias('multiply'), False),
    'divide': (lambda args: (args[0] / args[1]).alias('divide'), False),
    'if': (lambda args: case(args[0])
                   .when(literal(True), args[1])
                   .otherwise(args[2]).alias('if'), False),
    'and': (lambda args: reduce(lambda x, y: x & y, args).alias('and'), False),
    'gt': (lambda args: (args[0] > args[1]), False),
    'gte': (lambda args: (args[0] >= args[1]), False),  # Added
    'lt': (lambda args: (args[0] < args[1]), False),
    'lte': (lambda args: (args[0] <= args[1]), False),  # Added if needed
    # Add other functions as needed
}

def ast_to_datafusion_expr(ast, df_schema=None):
    if isinstance(ast, int):
        return literal(ast), False  # Literal number is not an aggregate

    if isinstance(ast, str):
        return literal(ast), False  # Literal string is not an aggregate

    if isinstance(ast, tuple):
        node_type = ast[0]

        if node_type == 'column':
            column_name = ast[1]
            if df_schema and column_name not in df_schema:
                raise ColumnNotFoundError(column_name)
            return col(column_name), False  # Column reference is not an aggregate

        elif node_type == 'string':
            return literal(ast[1]), False  # String literal

        elif node_type in FUNCTION_REGISTRY:
            args = []
            is_aggregate = False
            for arg in ast[1]:
                expr, agg = ast_to_datafusion_expr(arg, df_schema)
                args.append(expr)
                if agg:
                    is_aggregate = True

            func, func_is_aggregate = FUNCTION_REGISTRY[node_type]
            expr = func(args)
            is_aggregate = func_is_aggregate or is_aggregate
            return expr, is_aggregate
        else:
            raise InvalidOperationError(node_type, "Unknown AST node type")
    else:
        raise InvalidOperationError(str(ast), "Invalid AST node")
