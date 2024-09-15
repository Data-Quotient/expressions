
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDleftORnonassocGREATER_THANLESS_THANEQleftPLUSMINUSleftTIMESSLASHADD AND COLUMN COMMA DIVIDE EQ GREATER_THAN GT GTE IDENTIFIER IF LESS_THAN LPAREN LT LTE MINUS MULTIPLY NUMBER OR PLUS RPAREN SLASH STRING SUBTRACT SUM TIMESexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression SLASH expression\n                  | expression GREATER_THAN expression\n                  | expression LESS_THAN expression\n                  | expression EQ expressionexpression : LPAREN expression RPARENexpression : COLUMNexpression : STRINGexpression : NUMBERexpression : FUNCTION_NAME LPAREN arg_list RPAREN\n                  | IDENTIFIER LPAREN arg_list RPARENFUNCTION_NAME : IF\n                     | SUM\n                     | SUBTRACT\n                     | ADD\n                     | MULTIPLY\n                     | DIVIDE\n                     | AND\n                     | OR\n                     | GT\n                     | LT\n                     | GTE\n                     | LTEarg_list : expression\n                | arg_list COMMA expression'
    
_lr_action_items = {'LPAREN':([0,2,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,42,],[2,2,28,29,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,2,2,2,2,2,2,2,2,2,2,]),'COLUMN':([0,2,20,21,22,23,24,25,26,28,29,42,],[3,3,3,3,3,3,3,3,3,3,3,3,]),'STRING':([0,2,20,21,22,23,24,25,26,28,29,42,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'NUMBER':([0,2,20,21,22,23,24,25,26,28,29,42,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'IDENTIFIER':([0,2,20,21,22,23,24,25,26,28,29,42,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'IF':([0,2,20,21,22,23,24,25,26,28,29,42,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'SUM':([0,2,20,21,22,23,24,25,26,28,29,42,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'SUBTRACT':([0,2,20,21,22,23,24,25,26,28,29,42,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'ADD':([0,2,20,21,22,23,24,25,26,28,29,42,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'MULTIPLY':([0,2,20,21,22,23,24,25,26,28,29,42,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'DIVIDE':([0,2,20,21,22,23,24,25,26,28,29,42,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'AND':([0,2,20,21,22,23,24,25,26,28,29,42,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'OR':([0,2,20,21,22,23,24,25,26,28,29,42,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'GT':([0,2,20,21,22,23,24,25,26,28,29,42,],[16,16,16,16,16,16,16,16,16,16,16,16,]),'LT':([0,2,20,21,22,23,24,25,26,28,29,42,],[17,17,17,17,17,17,17,17,17,17,17,17,]),'GTE':([0,2,20,21,22,23,24,25,26,28,29,42,],[18,18,18,18,18,18,18,18,18,18,18,18,]),'LTE':([0,2,20,21,22,23,24,25,26,28,29,42,],[19,19,19,19,19,19,19,19,19,19,19,19,]),'$end':([1,3,4,5,30,31,32,33,34,35,36,37,41,43,],[0,-9,-10,-11,-1,-2,-3,-4,-5,-6,-7,-8,-12,-13,]),'PLUS':([1,3,4,5,27,30,31,32,33,34,35,36,37,39,41,43,44,],[20,-9,-10,-11,20,-1,-2,-3,-4,20,20,20,-8,20,-12,-13,20,]),'MINUS':([1,3,4,5,27,30,31,32,33,34,35,36,37,39,41,43,44,],[21,-9,-10,-11,21,-1,-2,-3,-4,21,21,21,-8,21,-12,-13,21,]),'TIMES':([1,3,4,5,27,30,31,32,33,34,35,36,37,39,41,43,44,],[22,-9,-10,-11,22,22,22,-3,-4,22,22,22,-8,22,-12,-13,22,]),'SLASH':([1,3,4,5,27,30,31,32,33,34,35,36,37,39,41,43,44,],[23,-9,-10,-11,23,23,23,-3,-4,23,23,23,-8,23,-12,-13,23,]),'GREATER_THAN':([1,3,4,5,27,30,31,32,33,34,35,36,37,39,41,43,44,],[24,-9,-10,-11,24,-1,-2,-3,-4,None,None,None,-8,24,-12,-13,24,]),'LESS_THAN':([1,3,4,5,27,30,31,32,33,34,35,36,37,39,41,43,44,],[25,-9,-10,-11,25,-1,-2,-3,-4,None,None,None,-8,25,-12,-13,25,]),'EQ':([1,3,4,5,27,30,31,32,33,34,35,36,37,39,41,43,44,],[26,-9,-10,-11,26,-1,-2,-3,-4,None,None,None,-8,26,-12,-13,26,]),'RPAREN':([3,4,5,27,30,31,32,33,34,35,36,37,38,39,40,41,43,44,],[-9,-10,-11,37,-1,-2,-3,-4,-5,-6,-7,-8,41,-26,43,-12,-13,-27,]),'COMMA':([3,4,5,30,31,32,33,34,35,36,37,38,39,40,41,43,44,],[-9,-10,-11,-1,-2,-3,-4,-5,-6,-7,-8,42,-26,42,-12,-13,-27,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,20,21,22,23,24,25,26,28,29,42,],[1,27,30,31,32,33,34,35,36,39,39,44,]),'FUNCTION_NAME':([0,2,20,21,22,23,24,25,26,28,29,42,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'arg_list':([28,29,],[38,40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',18),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',19),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',20),
  ('expression -> expression SLASH expression','expression',3,'p_expression_binop','parser.py',21),
  ('expression -> expression GREATER_THAN expression','expression',3,'p_expression_binop','parser.py',22),
  ('expression -> expression LESS_THAN expression','expression',3,'p_expression_binop','parser.py',23),
  ('expression -> expression EQ expression','expression',3,'p_expression_binop','parser.py',24),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',29),
  ('expression -> COLUMN','expression',1,'p_expression_column','parser.py',34),
  ('expression -> STRING','expression',1,'p_expression_string','parser.py',39),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',44),
  ('expression -> FUNCTION_NAME LPAREN arg_list RPAREN','expression',4,'p_expression_function','parser.py',49),
  ('expression -> IDENTIFIER LPAREN arg_list RPAREN','expression',4,'p_expression_function','parser.py',50),
  ('FUNCTION_NAME -> IF','FUNCTION_NAME',1,'p_FUNCTION_NAME','parser.py',54),
  ('FUNCTION_NAME -> SUM','FUNCTION_NAME',1,'p_FUNCTION_NAME','parser.py',55),
  ('FUNCTION_NAME -> SUBTRACT','FUNCTION_NAME',1,'p_FUNCTION_NAME','parser.py',56),
  ('FUNCTION_NAME -> ADD','FUNCTION_NAME',1,'p_FUNCTION_NAME','parser.py',57),
  ('FUNCTION_NAME -> MULTIPLY','FUNCTION_NAME',1,'p_FUNCTION_NAME','parser.py',58),
  ('FUNCTION_NAME -> DIVIDE','FUNCTION_NAME',1,'p_FUNCTION_NAME','parser.py',59),
  ('FUNCTION_NAME -> AND','FUNCTION_NAME',1,'p_FUNCTION_NAME','parser.py',60),
  ('FUNCTION_NAME -> OR','FUNCTION_NAME',1,'p_FUNCTION_NAME','parser.py',61),
  ('FUNCTION_NAME -> GT','FUNCTION_NAME',1,'p_FUNCTION_NAME','parser.py',62),
  ('FUNCTION_NAME -> LT','FUNCTION_NAME',1,'p_FUNCTION_NAME','parser.py',63),
  ('FUNCTION_NAME -> GTE','FUNCTION_NAME',1,'p_FUNCTION_NAME','parser.py',64),
  ('FUNCTION_NAME -> LTE','FUNCTION_NAME',1,'p_FUNCTION_NAME','parser.py',65),
  ('arg_list -> expression','arg_list',1,'p_arg_list','parser.py',69),
  ('arg_list -> arg_list COMMA expression','arg_list',3,'p_arg_list','parser.py',70),
]
