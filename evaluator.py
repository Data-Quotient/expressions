from datafusion import col, literal, functions as f
def ast_to_datafusion_expr(ast):
    """ Convert the parsed AST into a DataFusion expression and alias it. """
    if isinstance(ast, int):
        return literal(ast)  # Literal numbers
    
    node_type = ast[0]
    
    if node_type == 'column':
        column_name = ast[1]
        return col(column_name)  # Return a column expression
    
    elif node_type == 'binop':
        op = ast[1]
        left = ast_to_datafusion_expr(ast[2])
        right = ast_to_datafusion_expr(ast[3])
        
        if op == '+':
            return (left + right).alias('result')
        elif op == '-':
            return (left - right).alias('subtract')  # Alias as 'subtract'
        elif op == '*':
            return (left * right).alias('result')
        elif op == '/':
            return (left / right).alias('result')
        else:
            raise ValueError(f"Unknown operator {op}")
    
    elif node_type in ['add', 'subtract', 'multiply', 'divide', 'sum']:
        left = ast_to_datafusion_expr(ast[1])
        right = ast_to_datafusion_expr(ast[2])
        
        if node_type == 'subtract':
            return (left - right).alias('subtract')  # Alias subtraction as 'subtract'
        elif node_type == 'add':
            return (left + right).alias('result')
        elif node_type == 'multiply':
            return (left * right).alias('result')
        elif node_type == 'divide':
            return (left / right).alias('result')
        elif node_type == 'sum':
            return f.sum(left + right).alias('result')

    elif node_type == 'if':
        condition = ast_to_datafusion_expr(ast[1])
        true_value = ast_to_datafusion_expr(ast[2])
        false_value = ast_to_datafusion_expr(ast[3])
        
        return f.case().when(condition, true_value).otherwise(false_value).alias('result')

    else:
        raise ValueError(f"Unknown AST node {node_type}")