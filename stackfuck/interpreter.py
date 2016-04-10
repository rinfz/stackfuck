from copy import deepcopy

from stackfuck.parser import Parser
from stackfuck.stream import InputStream
from stackfuck.token import TokenStream


class StackfuckError(Exception):
    """ Generic Stackfuck interpretation error """


class Interpreter(object):

    def __init__(self, source_code):
        # set up
        self.source_code = source_code
        input_stream = InputStream(self.source_code)
        token_stream = TokenStream(input_stream)
        self.ast = Parser(token_stream).parse_full()
        self.running = True

        # operational variables
        self.stack = []
        self.variables = {}
        self.buffers = {}
        self.current_buffer = None

    def next_buffer_name(self):
        num = str(len(self.buffers))
        return ("0" * (5 - len(num))) + num

    def find_label_index(self, label):
        for i, node in enumerate(self.ast):
            if node.type == "$" and node.value == label:
                return i
        raise StackfuckError("Unable to locate label: {}".format(label))

    def run(self):
        i = 0
        while self.running:
            if i > len(self.ast):
                self.running = False
                break

            try:
                node = self.ast[i]
            except IndexError:
                break

            if node.type == 'P':
                self.stack.append(node.value)

            elif node.type == 'T':
                self.variables[node.value] = self.stack[-1]

            elif node.type == 'V':
                self.stack.append(self.variables[node.value])

            elif node.type == 'C':
                self.buffers[self.next_buffer_name()] = ''

            elif node.type == 'S':
                self.current_buffer = node.value

            elif node.type == 'O':
                print(self.buffers[self.current_buffer], end="")

            elif node.type == 'I':
                self.buffers[self.current_buffer] = input()

            elif node.type == 'G' or node.type == 'L':
                # duplicating since G is not possible with optimisation
                if self.stack[-1]:
                    i = self.find_label_index(node.value)
                    continue

            elif node.type == 'g':
                if self.stack[-1]:
                    i += int(node.value.lstrip('0'))
                    continue

            elif node.type == 'N' or node.type == 'l':
                # duplicating since N is not possible with optimisation
                if not self.stack[-1]:
                    i = self.find_label_index(node.value)
                    continue

            elif node.type == 'n':
                if not self.stack[-1]:
                    i += int(node.value.lstrip('0'))
                    continue

            elif node.type == 'K':
                i = self.find_label_index(node.value)
                continue

            elif node.type == 'X':
                exit(node.value)

            elif node.type == 'x':
                exit(self.stack[-1])

            elif node.type == '$':
                # labels found via ast so nothing needed here
                pass

            elif node.type == 'A':
                self.buffers[self.current_buffer] += node.value

            elif node.type == 'a':
                for elem in self.buffers[self.current_buffer]:
                    self.stack.append(elem)

            elif node.type == '?':
                self.buffers[self.current_buffer] = deepcopy(self.buffers[node.value])

            elif node.type == ')':
                self.stack = []

            elif node.type == '(':
                self.stack.pop()

            elif node.type == ';' or node.type == ':':
                f = (lambda x: x) if node.type == ';' else reversed
                for elem in f(self.stack):
                    if isinstance(elem, int):
                        # buffers are for ascii data
                        elem = chr(elem)
                    self.buffers[self.current_buffer] += elem

            elif node.type == '+':
                tmp = self.stack.pop()
                self.stack[-1] += tmp

            elif node.type == '-':
                tmp = self.stack.pop()
                self.stack[-1] -= tmp

            elif node.type == '/':
                tmp = self.stack.pop()
                self.stack[-1] /= self.stack[-1]

            elif node.type == '*':
                tmp = self.stack.pop()
                self.stack[-1] *= self.stack[-1]

            elif node.type == '^':
                tmp = int(bool(self.stack.pop()))
                self.stack[-1] = int(bool(self.stack[-1]))
                self.stack[-1] ^= tmp

            elif node.type == '|':
                tmp = int(bool(self.stack.pop()))
                self.stack[-1] = int(bool(self.stack[-1]))
                self.stack[-1] |= tmp

            elif node.type == '&':
                tmp = int(bool(self.stack.pop()))
                self.stack[-1] = int(bool(self.stack[-1]))
                self.stack[-1] &= tmp

            elif node.type == '\\':
                tmp = self.stack.pop()
                self.stack[-1] = self.stack[-1] or tmp

            elif node.type == '7':
                tmp = self.stack.pop()
                self.stack[-1] = self.stack[-1] and tmp

            elif node.type == 'Z':
                raise NotImplementedError("This feature is not available.")

            elif node.type == '<':
                tmp = self.stack.pop()
                self.stack[-1] = int(self.stack[-1] < tmp)

            elif node.type == '>':
                tmp = self.stack.pop()
                self.stack[-1] = int(self.stack[-1] > tmp)

            elif node.type == '.':
                tmp = self.stack.pop()
                self.stack[-1] = int(self.stack[-1] >= tmp)

            elif node.type == ',':
                tmp = self.stack.pop()
                self.stack[-1] = int(self.stack[-1] <= tmp)

            elif node.type == '=':
                tmp = self.stack.pop()
                self.stack[-1] = int(self.stack[-1] == tmp)

            elif node.type == '!':
                tmp = self.stack.pop()
                self.stack[-1] = int(self.stack[-1] != tmp)

            elif node.type == 'E':
                self.stack.append(int(self.current_buffer == node.value))

            i += 1
