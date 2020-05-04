import sys
from . import lex, yacc
from . import lexer as curr_lexer
from . import parser as curr_parser

current_lexer = lex.lex(module=curr_lexer)
try:
    assert len(sys.argv) == 2
    with open(sys.argv[1]) as input_file:
        all_tokens = input_file.read()
        current_lexer.input(all_tokens)
        for token in current_lexer:
            print(token)
        current_parser = yacc.yacc(module=curr_parser)
        parsed_data = current_parser.parse(all_tokens, lexer=current_lexer)
except (AssertionError, IndexError):
    print("The parameter can only be the filename to the system")
