from stackfuck.parser import Parser
from stackfuck.stream import InputStream
from stackfuck.token import TokenStream


class Interpreter(object):

    def __init__(self, source_code):
        self.source_code = source_code
        self.stack = []
        input_stream = InputStream(self.source_code)
        token_stream = TokenStream(input_stream)
        self.ast = Parser(token_stream).parse_full()

    def run(self):
        print('\n'.join(str(x) for x in self.ast))
