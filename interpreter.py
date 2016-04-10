#!/usr/bin/env python
import sys
from stackfuck.interpreter import Interpreter

if __name__ == '__main__':
    source_file = sys.argv[1]
    with open(source_file, 'r') as source:
        source_code = source.read()
    interpreter = Interpreter(source_code)
    interpreter.run()
