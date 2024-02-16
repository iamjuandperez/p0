import lexer as lex

class Stack:
    def __init__(self):
        self.tokens = []

    def is_empty(self):
        return len(self.tokens) == 0

    def push(self, token):
        self.tokens.append(token)

    def pope(self):
        if not self.is_empty():
            return self.tokens.pop()
        else:
            raise IndexError("The stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.tokens[-1]
        else:
            return None

    def size(self):
        return len(self.tokens)
    
def array_to_stack(arr):
    stack = Stack()
    for item in reversed(arr):
        stack.push(item)
    return stack

class Parser:
    def __init__(self, tokens):
        self.tokens = array_to_stack(tokens)
        self.tok_idx = 1
        self.advance()
        self.defun()

    def advance(self):

        self.current_tok = self.tokens.pope()
        return self.current_tok
    
    def defun(self): 
        if self.current_tok != 'varName':
            print('no')
        self.advance()
        if self.current_tok  != 'number':
            print('no')
        self.advance()
        if self.current_tok  != 'right':
            print('no')

    def move(self):
        if self.current_tok != 'number':
            print ('no')
        self.advance()
        if self.current_tok  != 'right':
            print('no')

    def skip(self):
        if self.current_tok != 'numer':
            print('no')
        if self.current_tok  != 'right':
            print('no')
    
    def turn(self):
        odds = ['tLeft', 'tRight', 'tAround']

    
def run (text):
    lexer = lex.iniciar(text)
    
    parser = Parser(lexer)

run("peludo 3)")
    