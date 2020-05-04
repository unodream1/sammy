from sammy.lexer import tokens


# Precedence rules for the arithmetic operators
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

# dictionary of names (for storing variables)
names = {}


def p_statement_single(p):
    """statement : NAME EQUALS expression END"""
    names[p[1]] = p[3]
    print(p[1], p[2], p[3])


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression AND expression
                  | expression OR expression'''
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]
    elif p[2] == "and": p[0] = p[1] and p[3]
    elif p[2] == "or": p[0] = p[1] or p[3]


def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]


def p_expression_true(p):
    'expression : TRUE'
    p[0] = 1


def p_expression_false(p):
    'expression : FALSE'
    p[0] = 0


def p_expression_name(p):
    'expression : NAME'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0


def p_error(p):
    print(f"Syntax error at {p.value!r}")
