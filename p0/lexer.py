tokens = []

def lexer(char):
    
    
        if char == '(':
            tokens.append('left')
        elif char == ')':
            tokens.append('right')
        elif char == '=':
            tokens.append('equal')
        elif char == 'defvar':
            tokens.append('defvar')
        elif char == 'name':
            tokens.append('name')
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

        return tokens
        
def separador (cadena : str ):
    cadena_separada = cadena.split(" ")
    for i in cadena_separada:
        if "(" in i:
            pos = i.find("(")
            lexer(i[pos])
            j = i[pos+1 : len(i)]
            lexer(j)
    

separador ("(defun name n)")
