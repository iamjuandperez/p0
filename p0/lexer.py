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
    elif char == 'pick':
            tokens.append('pick')
    elif char == 'move-dir':
            tokens.append('moveDir')
    elif char == 'move-face':
            tokens.append('moveFace')
    elif char == 'null':
            tokens.append('null') 
    elif char == 'if':
            tokens.append('conditional')
    elif char == 'facing?':
            tokens.append('cFacing')
    elif char == 'blocked?':
            tokens.append('cBlock') 
    elif char == 'can-put?':
            tokens.append('cCanput')
    elif char == 'can-pick?':
            tokens.append('cCanpick')
    elif char == 'can-move?':
            tokens.append('cCanmove')
    elif char == 'isZero?':
            tokens.append('cIszero')
    elif char == 'not':
            tokens.append('not') 
    elif char in ['Dim', 'myXpos', 'myYpos', 'myChips',
                  'myBalloons', 'balloonsHere', 'ChipsHere',
                  'Spaces']:
            tokens.append('constant')      
    elif char == '=':
            tokens.append('equal')                                                 
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