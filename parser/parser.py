import ply.yacc as yacc
from parser.lexer import tokens

# Precedence rules for arithmetic operations
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('nonassoc', 'GT', 'LT', 'EQ'),  # Add precedence for comparison operators
)

# Grammar rules

# Basic arithmetic and comparison operations
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression GT expression
                  | expression LT expression
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

# Function handling (e.g., IF, SUM, ADD, SUBTRACT)
def p_expression_function(p):
    '''expression : IF LPAREN expression COMMA expression COMMA expression RPAREN
                  | SUM LPAREN expression COMMA expression RPAREN
                  | SUBTRACT LPAREN expression COMMA expression RPAREN
                  | ADD LPAREN expression COMMA expression RPAREN
                  | MULTIPLY LPAREN expression COMMA expression RPAREN
                  | DIVIDE LPAREN expression COMMA expression RPAREN'''
    if p[1] == 'IF':
        p[0] = ('if', p[3], p[5], p[7])
    elif p[1] in ['SUM', 'SUBTRACT', 'ADD', 'MULTIPLY', 'DIVIDE']:
        p[0] = (p[1].lower(), p[3], p[5])

# Error handling rule
def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Build the parser
parser = yacc.yacc()
