class InputStreamError(Exception):
    """ An error occurred while reading source input """

class InputStream(object):

    def __init__(self, data):
        self.data = data
        self.pos = 0
        self.line = 1
        self.col = 0

    def next(self):
        self.pos += 1
        ch = self.data[self.pos]
        if ch == '\n':
            self.line += 1
            self.col = 0
        else:
            self.col += 1
        return ch

    def peek(self):
        return self.data[self.pos]

    def eof(self):
        try:
            self.peek()
            return False
        except IndexError:
            return True

    def croak(self, message="An unknown error occurred"):
        raise InputStreamError("{} at line {}, col {}".format(message, self.line, self.col))
