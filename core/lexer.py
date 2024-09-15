# core/lexer.py

import ply.lex as lex

# Define reserved words
reserved = {
    'IF': 'IF',
    'THEN': 'THEN',
    'ELSE': 'ELSE',
    'END': 'END',
    'ELSEIF': 'ELSEIF', 
    'SUM': 'SUM',
    'SUBTRACT': 'SUBTRACT',
    'ADD': 'ADD',
    'MULTIPLY': 'MULTIPLY',
    'DIVIDE': 'DIVIDE',
    'AND': 'AND',
    'OR': 'OR',
    'GT': 'GT',
    'LT': 'LT',
    'GTE': 'GTE',  # Added
    'LTE': 'LTE',  # You might want to add this as well
    # Add other function names as needed
}

# Define the list of token names
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'SLASH',
    'LPAREN', 'RPAREN', 'COLUMN', 'GREATER_THAN', 'LESS_THAN', 'EQ',
    'COMMA', 'STRING', 'IDENTIFIER',
) + tuple(reserved.values())

# Define simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_SLASH = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_EQ = r'=='
t_COMMA = r','

# Handle string literals (single-quoted strings)
def t_STRING(t):
    r'\'(.*?)\''
    t.value = t.value.strip("'")  # Remove the surrounding single quotes
    return t

# Handle column names (double-quoted strings)
def t_COLUMN(t):
    r'\"(.*?)\"'
    t.value = t.value.strip('"')  # Remove the surrounding double quotes
    return t

# Handle identifiers and reserved words
def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value.upper(), 'IDENTIFIER')  # Check for reserved words
    return t

# Handle number literals
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Error handling for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
