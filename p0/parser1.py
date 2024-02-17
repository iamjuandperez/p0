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
        
    def next_token(self):
        if not self.is_empty() and len(self.tokens) > 1:
            return self.tokens[-1]
        else:
            return "No next item"

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
        self.run()
        print(tokens)
        
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
        if self.current_tok != 'number':
            print('no')
        self.advance()
        if self.current_tok  != 'right':
            print('nop')
    
    def rundirs(self):
        odds = ['tUp', 'tRight', 'tLeft', 'tDown']
        if self.current_tok not in odds:
            print('no')
        self.advance()
        while  self.tokens.next_token() in odds:
            self.advance()
        self.advance()
        if self.current_tok != 'right':
            print('no')
    
    def face(self):
        direcc = ['fNorth', 'fSouth', 'fEast', 'fWest']
        if self.current_tok not in direcc:
            print('no')
        self.advance()
        if self.current_tok != 'right':
            print('no')
    
    def turn(self):
        odds = ['tLeft', 'tRight', 'tAround']
        if self.current_tok not in odds:
            print('no')
        self.advance()
        if self.current_tok != 'right':
            print('no')
            
    def put(self):
        if self.current_tok != 'object':
            print('no')
        self.advance()
        if self.current_tok != 'number':
            print('no')
        self.advance()
        if self.current_tok != 'right':
            print('no')
            
    def pick(self):
        if self.current_tok != 'object':
            print('no')
        self.advance()
        if self.current_tok != 'number':
            print('no')
        self.advance()
        if self.current_tok != 'right':
            print('no')
    
    def movedir(self):
        if self.current_tok != 'number':
            print('no')
        odds = ['tLeft', 'tRight', 'tFront', 'tBack']
        self.advance
        if self.current_tok not in odds:
            print('no')
        self.advance()
        if self.current_tok != 'right':
            print('no')
    
    def moveFace(self):
        if self.current_tok != 'number':
            print('no')
        self.advance()
        direcc = ['fNorth', 'fSouth', 'fEast', 'fWest']
        if self.current_tok not in direcc:
            print('no')
        self.advance()
        if self.current_tok != 'right':
            print('no')

    def run (self):
        while not self.tokens.is_empty():
           
            if self.current_tok != 'left':
               print ('no')
            self.advance()
            if self.current_tok == 'defun':
               self.advance()
               self.defun()
            elif self.current_tok == 'move':
                self.advance()
                self.move()
            elif self.current_tok == 'skip':
                self.advance()
                self.skip()
            elif self.current_tok == 'rundirs':
                self.advance()
                self.rundirs()
            elif self.current_tok == 'face':
                self.advance()
                self.face()
            elif self.current_tok ==  'turn':
                self.advance()
                self.turn()
            elif self.current_tok == 'put':
                self.advance()
                self.put()
            else: 
                print('no')
            if not self.tokens.is_empty():
               self.advance()
               
               
        
        
def run (text):
    lexer = lex.iniciar(text)
    Parser(lexer)

run("(defun var 5)   (skip 1)                                      (move 34)(run-dirs :left :up :left :down :right)")
    