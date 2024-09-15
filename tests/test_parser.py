import pytest
from core.parser import parser

def test_parse_sum():
    data = 'SUM("salary")'
    result = parser.parse(data)
    expected_ast = ('sum', [('column', 'salary')])
    assert result == expected_ast

def test_parse_if():
    data = 'IF(GT("salary", 6000), \'High\', \'Low\')'
    result = parser.parse(data)
    expected_ast = ('if', [('gt', [('column', 'salary'), 6000]), ('string', 'High'), ('string', 'Low')])
    assert result == expected_ast

def test_parse_add():
    data = 'ADD("salary", "bonus")'
    result = parser.parse(data)
    expected_ast = ('add', [('column', 'salary'), ('column', 'bonus')])
    assert result == expected_ast
