# core/parser.py
import ply.yacc as yacc
from core.lexer import tokens

# Precedence rules for arithmetic and comparison operations
# Precedence rules for arithmetic, comparison, and conditional operators
precedence = (
    ('left', 'AND'),
    ('left', 'OR'),
    ('nonassoc', 'GREATER_THAN', 'LESS_THAN', 'EQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'SLASH'),
    ('right', 'IF'),  # Give precedence to IF
)

# Grammar rules

# Expression parsing
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

# Column references
def p_expression_column(p):
    'expression : COLUMN'
    p[0] = ('column', p[1])

# String literals
def p_expression_string(p):
    'expression : STRING'
    p[0] = ('string', p[1])

# Numbers
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

# Function handling
def p_expression_function(p):
    '''expression : FUNCTION_NAME LPAREN arg_list RPAREN
                  | IDENTIFIER LPAREN arg_list RPAREN'''
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
                     | LT
                     | GTE
                     | LTE'''
    p[0] = p[1]

def p_arg_list(p):
    '''arg_list : expression
                | arg_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# New rules for if-else and else if (CASE handling)
def p_expression_if(p):
    '''expression : IF expression THEN expression if_expression_tail END'''
    # Build a list of (condition, expression) tuples
    p[0] = ('if_chain', [(p[2], p[4])] + p[5])

def p_if_expression_tail(p):
    '''if_expression_tail : ELSEIF expression THEN expression if_expression_tail
                          | ELSE expression
                          | empty'''
    if len(p) == 6:
        # More ELSEIF clauses
        p[0] = [(p[2], p[4])] + p[5]
    elif len(p) == 3:
        # ELSE clause
        p[0] = [('else', p[2])]
    else:
        # No more clauses
        p[0] = []

# Handle empty rule
def p_empty(p):
    'empty :'
    pass

# Error handling rule
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
