# core/parser.py

import ply.yacc as yacc
from core.lexer import tokens

# Precedence rules for arithmetic and comparison operations
precedence = (
    ('left', 'AND'),
    ('left', 'OR'),
    ('nonassoc', 'GREATER_THAN', 'LESS_THAN', 'EQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'SLASH'),
)
# Grammar rules

## Expression parsing
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression SLASH expression
                  | expression GREATER_THAN expression
                  | expression LESS_THAN expression
                  | expression EQ expression'''
    p[0] = ('binop', p[2], p[1], p[3])


# Parentheses
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

# Column references or strings
def p_expression_column(p):
    '''expression : COLUMN
                  | STRING'''
    p[0] = ('column', p[1])

# Numbers
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

# Function handling
def p_expression_function(p):
    '''expression : FUNCTION_NAME LPAREN arg_list RPAREN'''
    p[0] = (p[1].lower(), p[3])

def p_FUNCTION_NAME(p):
    '''FUNCTION_NAME : IF
                     | SUM
                     | SUBTRACT
                     | ADD
                     | MULTIPLY
                     | DIVIDE
                     | AND
                     | OR
                     | GT
                     | LT'''
    p[0] = p[1]

def p_arg_list(p):
    '''arg_list : expression
                | arg_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# Error handling rule
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()