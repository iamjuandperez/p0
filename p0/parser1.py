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
            exit()
        
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
        self.correcto = True
       
        self.advance()
        self.run()
        
    def advance(self):

        self.current_tok = self.tokens.pope()
        return self.current_tok
    
    def defun(self): 
        
        if self.current_tok not in ['varName', 'cBlock']:
            print('no')
            self.correcto = False
            
        self.advance()
        
        if self.current_tok  != 'left':
            print('no')
            self.correcto = False
            
        self.advance()
        
        if self.current_tok  not in ['varName', 'right']:
            print('no')
            self.correcto = False
            
        if self.current_tok == 'varName':
            self.advance()
            self.parametros()
            
        elif self.current_tok == 'right':
            self.advance()
            
        if self.current_tok != 'left':
            print('no')
            self.correcto = False

        if self.tokens.next_token() in ['conditional', 'not']:
            self.advance()
            self.advance()
            self.conditional()
            
        else:
            self.run()
            
        self.advance()
        
        if self.current_tok == 'left':
            self.run()
            
        elif self.current_tok != 'right':
            print('no')
            self.correcto = False
        
        
    def parametros (self):
        
        if self.current_tok == 'right':
            self.advance()
            
        else:
            if self.current_tok != 'varName':
                print('no')
                self.correcto = False
                
            else:
                self.advance()
                self.parametros()
         
                
    def move(self):
        
        var = ['number', 'constant', 'varName']
        if self.current_tok not in var:
            print ('no')
            self.correcto = False
            
        self.advance()
        
        if self.current_tok  != 'right':
            print('no')
            self.correcto = False


    def skip(self):
        
        var = ['number', 'constant', 'varName']
        if self.current_tok not in var:
            print('no')
            self.correcto = False
            
        self.advance()
        
        if self.current_tok  != 'right':
            print('no')
            self.correcto = False
    
    
    def rundirs(self):
        
        odds = ['tUp', 'tRight', 'tLeft', 'tDown']
        if self.current_tok not in odds:
            print('no')
            self.correcto = False
            
        self.advance()
        
        while  self.tokens.next_token() in odds:
            self.advance()
            
        self.advance()
        
        if self.current_tok != 'right':
            print('no')
            self.correcto = False
    
    
    def face(self):
        
        direcc = ['fNorth', 'fSouth', 'fEast', 'fWest']
        if self.current_tok not in direcc:
            print('no')
            self.correcto = False
            
        self.advance()
        
        if self.current_tok != 'right':
            print('no')
            self.correcto = False
    
    
    def turn(self):
        
        odds = ['tLeft', 'tRight', 'tAround']
        if self.current_tok not in odds:
            print('no')
            self.correcto = False
            
        self.advance()
        
        if self.current_tok != 'right':
            print('no')
            self.correcto = False
            
            
    def put(self):
        
        if self.current_tok != 'object':
            print('no')
            self.correcto = False
            
        self.advance()
        
        var = ['number', 'constant', 'varName']
        if self.current_tok not in var:
            print('no')
            self.correcto = False
            
        self.advance()
        
        if self.current_tok != 'right':
            print('no')
            self.correcto = False
        
            
    def pick(self):
        
        if self.current_tok != 'object':
            print('no')
            self.correcto = False
            
        self.advance()
        
        var = ['number', 'constant', 'varName']
        if self.current_tok not in var:
            print('no')
            self.correcto = False
            
        self.advance()
        
        if self.current_tok != 'right':
            print('no')
            self.correcto = False
    
    
    def movedir(self):
        
        var = ['number', 'constant', 'varName']
        if self.current_tok not in var:
            print('no')
            self.correcto = False
            
        self.advance()
        
        odds = ['tLeft', 'tRight', 'tFront', 'tBack']
        if self.current_tok not in odds:
            print('no')
            self.correcto = False
            
        self.advance()
        
        if self.current_tok != 'right':
            print('no')
            self.correcto = False
    
    
    def moveFace(self):
        
        var = ['number', 'constant', 'varName']
        if self.current_tok not in var:
            print('no')
            self.correcto = False
            
        self.advance()
        
        direcc = ['fNorth', 'fSouth', 'fEast', 'fWest']
        if self.current_tok not in direcc:
            print('no')
            self.correcto = False
            
        self.advance()
        
        if self.current_tok != 'right':
            print('no')
            self.correcto = False
    
    
    def nulo(self):
        
        if self.current_tok != 'right':
            print('no')
            self.correcto = False
    
    
    def conditional(self):
        
        if self.current_tok != 'left':
            print('no')
            self.correcto = False
            
        self.advance()
        
        if self.current_tok in ['cFacing', 'cCanmove']:
            direcc = ['fNorth', 'fSouth', 'fEast', 'fWest']
            
            self.advance()
            
            if self.current_tok not in direcc:
                print('no')
                self.correcto = False
                
            self.advance()
            
            if self.current_tok != 'right':
                print('no')
                self.correcto = False
                
        elif self.current_tok == 'cBlock':
            self.advance()
            
            if self.current_tok != 'right':
                print('no')
                self.correcto = False
        
        elif self.current_tok in ['cCanput', 'cCanpick']:
            self.advance()
            
            if self.current_tok != 'object':
                print('no')
                self.correcto = False
                
            self.advance()
            
            var = ['number', 'constant', 'varName']
            if self.current_tok not in var:
                print('no')
                self.correcto = False
                
            self.advance()
            
            if self.current_tok != 'right':
                print('no')
                self.correcto = False
        
        elif self.current_tok == 'cIszero':
            self.advance()
            
            var = ['number', 'constant', 'varName']
            if self.current_tok not in var:
                print('no')
                self.correcto = False
                
            self.advance()
            
            if self.current_tok != 'right':
                print('no')  
                self.correcto = False  
        
        elif self.current_tok == 'not':
            self.advance()
            self.conditional()
            
        else:
            print('no')
            self.correcto = False

        if self.current_tok != 'right':
            print('no')
            self.correcto = False
        
        
    def VariableCrea(self):
        
        if self.current_tok != 'varName':
            print('no')
            self.correcto = False
             
        self.advance()
        
        if self.current_tok != 'right':
            print('no')
            self.correcto = False
    
    
    def defvar(self):
        
        if self.current_tok != 'varName':
            print('no')
            self.correcto = False
            
        self.advance()
        
        var = ['number', 'constant', 'varName']
        if self.current_tok not in var:
            print('no')
            self.correcto = False
            
        self.advance()
        
        if self.current_tok != 'right':
            print('no')
            self.correcto = False
    
    
    def loop(self):
        
        condit = [
            'cFacing', 'cBlock', 'cCanput',
            'cCanpick', 'cCanmove', 'cIszero'
            ]
        if self.current_tok not in condit:
            print('no')
            self.correcto = False
            
        self.advance()
        self.run()
    
    
    def repeat(self):
        
        var = ['number', 'constant', 'varName']
        if self.current_tok not in var:
            print('no')
            self.correcto = False
            
        self.advance()
        self.run()
    
    
    def actFunction(self):
        
        if self.current_tok == 'right':
            self.advance()
        
        var = ['number', 'constant', 'varName']
        if self.current_tok not in var:  
            self.advance()
            self.actFunction()
            
        else:
            print('no')
            self.correcto = False


    def run(self):
        
        while not self.tokens.is_empty() and self.correcto:
           
            if self.tokens.next_token() == 'left':
                self.advance()
                self.run()
                self.advance()
                
                if self.current_tok != 'right':
                    print('no')
                    self.correcto = False
                    
            elif self.current_tok != 'left':
               print ('no')
               self.correcto = False
               
            self.advance()
            
            if self.current_tok == 'defun':
               self.advance()
               self.defun()
               
            elif self.current_tok == 'defvar':
                self.advance()
                self.defvar()
                
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
                
            elif self.current_tok == 'pick':
                self.advance()
                self.put()
                
            elif self.current_tok == 'moveDir':
                self.advance()
                self.movedir()
                
            elif self.current_tok == 'moveFace':
                self.advance()
                self.moveFace
                
            elif self.current_tok == 'null':
                self.advance()
                self.nulo()   
                 
            elif self.current_tok == 'conditional':
                self.advance()
                self.conditional()
                
            elif self.current_tok == 'equal':
                self.advance()
                self.VariableCrea()
            
            elif self.current_tok == 'loop':
                self.advance()
                self.loop()
            
            elif self.current_tok == 'repeat':
                self.advance()
                self.repeat()
            
            elif self.current_tok == 'varName':
                self.advance()
                self.actFunction()
            
            else: 
                print('no')
                self.correcto = False
                
            if not self.tokens.is_empty() and self.current_tok != 'left':
               self.advance()
        
        if self.correcto:
            print('yes')
        
               
    
def run (text):
    
    lexer = lex.iniciar(text)
    Parser(lexer)

prueba = '(if (blocked-p) (move 1) (skip 3))'

run(prueba)