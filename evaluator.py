from datafusion import col, literal, functions as f

def ast_to_datafusion_expr(ast):
    """ Convert the parsed AST into a DataFusion expression. """
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
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right
        else:
            raise ValueError(f"Unknown operator {op}")
    
    elif node_type in ['add', 'subtract', 'multiply', 'divide', 'sum']:
        left = ast_to_datafusion_expr(ast[1])
        right = ast_to_datafusion_expr(ast[2])
        
        if node_type == 'subtract':
            return left - right
        elif node_type == 'add':
            return left + right
        elif node_type == 'multiply':
            return left * right
        elif node_type == 'divide':
            return left / right
        elif node_type == 'sum':
            return f.sum(left + right)
    
    elif node_type == 'if':
        condition = ast_to_datafusion_expr(ast[1])
        true_value = ast_to_datafusion_expr(ast[2])
        false_value = ast_to_datafusion_expr(ast[3])
        
        return
