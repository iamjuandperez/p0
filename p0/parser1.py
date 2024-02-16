import lexer as lex

class Stack:
    def __init__(self):
        self.tokens = []

    def is_empty(self):
        return len(self.tokens) == 0

    def push(self, token):
        self.tokens.append(token)

    def pop(self):
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

class Parser:
    def __init__(tokens):
        self.tokens = tokens
        self.tok_idx = 1
        self.advance()

    def advance( ):
        self.tok_idx +=1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]

  