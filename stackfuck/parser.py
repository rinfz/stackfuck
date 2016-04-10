from stackfuck.token import Token


class Parser(object):

    def __init__(self, token_stream):
        self.token_stream = token_stream
        self.ast = []

    def parse_full(self):
        # build the initial ast
        self.parse_toplevel()
        # optimisations (in-place)
        self.squash_pushes()
        return self.ast

    def parse_toplevel(self):
        while not self.token_stream.data.eof():
            self.ast.append(self.token_stream.read_next())

    def squash_pushes(self):
        new_ast = []
        push = []
        for node in self.ast:
            if node.type == "P" and isinstance(node.value, str):
                push.append(node.value)
                continue
            elif push:
                new_ast.append(Token(type="P", value=''.join(push)))
                push = []
            new_ast.append(node)
        self.ast = new_ast
