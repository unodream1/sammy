tokens = ["NAME", "NUMBER", "PLUS", "MINUS", "TIMES", "DIVIDE", "EQUALS", "LPAREN", "RPAREN",
          "STRING", "END"]
reserved = {"true": "TRUE", "false": "FALSE", "and": "AND", "or": "OR"}
tokens = tokens + list(reserved.values())
t_ignore = " \t|\n"
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_EQUALS = r"="
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_STRING = r'"[a-zA-Z_][a-zA-Z0-9_]*"'
t_END = ";"


def t_NAME(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t


def t_NUMBER(t):
    # r'\d+'
    r'[0-9]*\.[0-9]+|[0-9]+'
    t.value = float(t.value) if ("." in t.value) else int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.skip(1)


def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)