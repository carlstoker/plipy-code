# Cuppa2 interpreter

from cuppa2_symtab import symbol_table
from cuppa2_fe import parse
from cuppa2_interp_walk import walk
from dumpast import dumpast

def interp(input_stream, dump=False):
    try:
        symbol_table.initialize()
        ast = parse(input_stream)
        if dump:
            dumpast(ast)
        else:
            walk(ast)
    except Exception as e:
        print("error: "+str(e))
    return None

if __name__ == "__main__":
    import sys
    import os

    ast_switch = False
    char_stream = ''

    if len(sys.argv) == 1: # no args - read stdin
        char_stream = sys.stdin.read()
    else:
        # if there is a '-d' switch use it
        ast_switch = sys.argv[1] == '-d'
        # last arg is the filename to open and read
        input_file = sys.argv[-1]
        if not os.path.isfile(input_file):
            print("unknown file {}".format(input_file))
            sys.exit(0)
        else:
            f = open(input_file, 'r')
            char_stream = f.read()
            f.close()

    interp(char_stream, dump=ast_switch)
