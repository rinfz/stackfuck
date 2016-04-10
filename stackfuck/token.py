from stackfuck.keywords import INSTRUCTIONS, INSTRUCTIONS_WITH_ARGS


class Token(object):

    def __init__(self, **kwargs):
        assert 'type' in kwargs
        assert 'value' in kwargs

        # attributes of the token can be fairly arbitrary so just accept
        # everything so long as we already have a type and value
        self.__dict__.update(kwargs)


class TokenStream(object):

    def __init__(self, data):
        self.data = data
        self.keywords = INSTRUCTIONS
        self.current = None

    def is_keyword(self, ch):
        return ch in self.keywords

    def has_args(self, ch):
        return ch in INSTRUCTIONS_WITH_ARGS.keys()

    def is_digit(self, ch):
        return ch.isdigit()

    def is_whitespace(ch):
        return ch in " \t\n"

    def read_while(self, pred):
        val = []
        while not self.data.eof() and pred(self.data.peek()):
            val.append(self.data.next())
        return ''.join(val)

    def read_number(self):
        has_dot = False
        def _read_number(ch):
            nonlocal has_dot
            if ch == ".":
                if has_dot:
                    return False
                has_dot = True
                return True
            return self.is_digit(ch)
        number = self.read_while(_read_number)
        cast = float if has_dot else int
        return Token(type="num", value=cast(number))

    def read_push(self):
        # special case for push (P) since it has variable length args
        if self.data.peek(offset=1) == 'x':
            # reading a char
            self.data.next() # discard the 'x' used to denote that its a char
            value = self.data.next()
        else:
            # reading a number
            value = ''.join(self.data.next() for _ in range(3))
            if '.' in value:
                value = float(value)
            else:
                value = int(value.lstrip('0'))
        return Token(type="call", func="P", value=value)

    def read_kw_with_args(self, ch):
        value = ''.join(self.data.next() for _ in range INSTRUCTIONS_WITH_ARGS[ch])
        return Token(type="call", func=ch, value=value)

    def _skip_comment(self, ch):
        return ch != '\n'

    def skip_comment(self):
        self.read_while(self._skip_comment)

    def read_next(self):
        read_while(self.is_whitespace)
        if self.data.eof():
            return None
        ch = self.data.peek()
        if ch == '#':
            self.skip_comment()
            return self.read_next()
        if self.has_args(ch):
            if ch == 'P':
                return self.read_push()
            else:
                return self.read_kw_with_args(ch)
        if self.is_keyword(ch):
            return Token(type="call", func=ch, value=None)
        self.data.croak("Can't handle character: {}".format(ch))

    def peek(self):
        if not self.current:
            self.current = self.read_next()
        return self.current

    def next(self):
        tok = self.current
        self.current = None
        return tok or self.read_next()

    def eof(self):
        return self.peek() == None
