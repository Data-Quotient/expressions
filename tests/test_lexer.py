import pytest
from core.lexer import lexer

def test_lexer_sum_token():
    data = 'SUM("salary")'
    lexer.input(data)
    tokens = [tok.type for tok in lexer]
    expected_tokens = ['SUM', 'LPAREN', 'COLUMN', 'RPAREN']
    assert tokens == expected_tokens

def test_lexer_if_token():
    data = 'IF(GT("salary", 6000), \'High\', \'Low\')'
    lexer.input(data)
    tokens = [tok.type for tok in lexer]
    expected_tokens = ['IF', 'LPAREN', 'GT', 'LPAREN', 'COLUMN', 'COMMA', 'NUMBER', 'RPAREN', 'COMMA', 'STRING', 'COMMA', 'STRING', 'RPAREN']
    assert tokens == expected_tokens

def test_lexer_add_token():
    data = 'ADD("salary", "bonus")'
    lexer.input(data)
    tokens = [tok.type for tok in lexer]
    expected_tokens = ['ADD', 'LPAREN', 'COLUMN', 'COMMA', 'COLUMN', 'RPAREN']
    assert tokens == expected_tokens
