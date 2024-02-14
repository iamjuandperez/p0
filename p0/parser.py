import lexer as lex

arbolReglas = 

def parser(cadena):
    res = True
    arreglo = lex.iniciar(cadena)
    if arreglo[0] != 'left' or arreglo[len(arreglo)] != 'right':
        res = False
        return res
    i = 0
    while res and i < len(arreglo):
        