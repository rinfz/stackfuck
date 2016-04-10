from stackfuck.parser import Parser
from stackfuck.stream import InputStream
from stackfuck.token import TokenStream


class Interpreter(object):

    def __init__(self, source_code):
        self.source_code = source_code

    def run(self):
        input_stream = InputStream(self.source_code)
        token_stream = TokenStream(input_stream)
        parser = Parser(token_stream)
        parser.parse_full()
        print('\n'.join(str(x) for x in parser.ast))
