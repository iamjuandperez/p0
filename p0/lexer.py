tokens = []

def lexer(char):
    
    if char.isdigit():
        tokens.append("number")
    elif char == '(':
            tokens.append('left')
    elif char == ')':
            tokens.append('right')
    elif char == '=':
            tokens.append('equal')
    elif char == 'defvar':
            tokens.append('defvar')
    elif char == 'skip':
            tokens.append('skip')
    elif char == 'turn':
            tokens.append('turn')
    elif char == ':left':
            tokens.append('tLeft')
    elif char == ':right':
            tokens.append('tRight')
    elif char == ':around':
            tokens.append('tAround')
    elif char == 'face':
            tokens.append('face')
    elif char == ':north':
            tokens.append('fNorth')
    elif char == ':south':
            tokens.append('fSouth')
    elif char == ':east':
            tokens.append('fEast')
    elif char == ':west':
            tokens.append('fWest')
    elif char == 'turn':
            tokens.append('turn')
    elif char == 'left':
            tokens.append('tLeft')
    elif char == 'right':
            tokens.append('tRight')
    elif char == 'around':
            tokens.append('around')    
    elif char == 'defun':
            tokens.append('defun')
    elif char == ':balloons' or char == ':chips':
            tokens.append('object')
    elif char == ':front':
            tokens.append('tFront')
    elif char == ':back':
            tokens.append('tBack')
    elif char == ':up':
           tokens.append('tUp')
    elif char == ':down':
           tokens.append('tDown')
    elif char == 'run-dirs':
           tokens.append('rundirs')
    elif char == 'move':
           tokens.append('move')
    else:
            tokens.append('varName')

    return tokens
        
def separador (texto : str ):
    
    
    parentesis = ['(', ')']
    for caracter in parentesis:
        if caracter not in ['(', ')']:
            texto = texto.replace(caracter, ' ')
    

    texto = texto.replace('(', ' ( ').replace(')', ' ) ')
    
    
    palabras = texto.split()
    
    return palabras

    

def iniciar(cadena):
    tok = separador(cadena)
    for i in tok:
       lexer(i)
    return tokens