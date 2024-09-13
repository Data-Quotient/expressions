import ply.lex as lex

# Define reserved words like IF, SUM, SUBTRACT, etc.
reserved = {
    'IF': 'IF',
    'SUM': 'SUM',
    'SUBTRACT': 'SUBTRACT',
    'ADD': 'ADD',
    'MULTIPLY': 'MULTIPLY',
    'DIVIDE': 'DIVIDE'
}

# Define the list of token names
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
    'LPAREN', 'RPAREN', 'COLUMN', 'GT', 'LT', 'EQ',
    'COMMA', 'STRING'
) + tuple(reserved.values())  # Include reserved words

# Define simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GT = r'>'
t_LT = r'<'
t_EQ = r'=='
t_COMMA = r','

# Handle column names (e.g., A, B, C1, etc.)
def t_COLUMN(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value.upper(), 'COLUMN')  # Check for reserved words
    return t

# Handle string literals (e.g., "salary", "tax")
def t_STRING(t):
    r'\".*?\"'
    t.value = t.value.strip('"')  # Remove the surrounding quotes
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
