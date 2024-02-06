def lexer(exp):
    tokens = []
    for char in exp:
        if char == '(':
            tokens.append('left', char)
        elif char == ')':
            tokens.append('right', char)
        elif char == '=':
            tokens.append('equal', char)
        elif char == 'defvar':
            tokens.append('defvar', char)
        elif char == 'name':
            tokens.append('name', char)
        elif char == 'skip':
            tokens.append('skip', char)
        elif char == 'turn':
            tokens.append('turn', char)
        elif char == ':left':
            tokens.append('tLeft', char)
        elif char == ':right':
            tokens.append('tRight', char)
        elif char == ':around':
            tokens.append('tAround')
        elif char == 'face':
            tokens.append('face', char)
        elif char == ':north':
            tokens.append('fNorth', char)
        elif char == ':south':
            tokens.append('fSouth', char)
        elif char == ':east':
            tokens.append('fEast', char)
        elif char == ':west':
            tokens.append('fWest', char)
        elif char == 'turn':
            tokens.append('turn', char)
        elif char == 'left':
            tokens.append('tLeft', char)
        elif char == 'right':
            tokens.append('tRight', char)
        elif char == 'around':
            tokens.append('around')    