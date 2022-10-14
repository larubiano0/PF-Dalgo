# Sebastián Gaona, Isaac Bermudez, Luis Rubiano
import sys
from math import sqrt, floor


def es_triangular(substring):
    if substring[0] == substring[1]:
        return True
    else:
        return False


def es_optimo(string, substring, k, triangular):
    if triangular:
        if k == len(string)*(len(string)-1)//2:
            return True
        else:
            return False
    else:
        if k == (len(string)**2)//4:
            return True
        else:
            return False


def contar(string, substring, triangular):
    '''
    Cuenta el número de veces que aparece substring en string
    '''
    apariciones = 0  # Numero total de apariciones de substring en string
    Na = 0  # Veces que aparece el primer caracter de substring en string
    a = substring[0]  # primer caracter de substring
    b = substring[1]  # segundo caracter de substring

    if not triangular:  # En caso de que los caracteres del substring sean distintos

        i = 0

        while i < len(string):  # Itera sobre el string de izquierda a derecha

            if string[i] == a:

                Na += 1  # Incremente el número de apariciones del primer caracter de substring en string

            elif string[i] == b:

                apariciones += Na  # Si el segundo caracter de substring aparece en string, incremente el número de apariciones de substring en string

            i += 1

        return apariciones

    else:  # En caso de que los caracteres del substring sean iguales

        i = 0

        while i < len(string):  # Itera sobre el string de izquierda a derecha

            if string[i] == substring[0]:

                Na += 1  # Cuenta las veces que aparece el caracter en el string

            i += 1

        # Retorna el número triangular asociado al número de apariciones del caracter en string
        return Na*(Na-1)//2


def subrutina(string, substring, a,b):
    i = 0
    while i < len(string):
        if string[i] != substring[0]:
            if string[i] == substring[1]:
                b -= 1
            a += 1
            string = string[:i] + substring[0] + string[i+1:]
            i = len(string)
        i += 1
    return string, a, b


def mejorar(string, substring, a = None, b = None):
    if not a:
        a, b = 0, 0 
        for i in string:
            if i == substring[0]:
                a += 1
            elif i == substring[1]:
                b += 1
    
    if a<b:
        string,a,b = subrutina(string, substring, a, b)
    elif a>b:
        string,b,a = subrutina(string[::-1], substring[::-1], b, a)
        string = string[::-1]
    else:
        string1,a1,b1 = subrutina(string, substring, a, b)
        string2,b2,a2 = subrutina(string[::-1], substring[::-1], b, a)
        string2 = string2[::-1]

        c1 = contar(string1, substring, es_triangular(substring))
        c2 = contar(string2, substring, es_triangular(substring))

        if c1>c2:
            string, a, b = string1, a1, b1
        elif c2>=c1:
            string, a, b = string2, a2, b2

    return string
                

if __name__ == "__main__":
    casos = int(sys.stdin.readline())  # Lee el número de casos
    for __ in range(casos):
        caso = sys.stdin.readline()
        string, substring, reemplazos = tuple(caso.split())
        reemplazos = int(reemplazos)

        triangular = es_triangular(substring)
        apariciones = contar(string, substring, triangular)

        if not es_optimo(string, substring, apariciones, triangular):
            # Si es el optimo, no importa el número de reemplazos no puede mejorar más
            if triangular:

                while reemplazos > 0:
                    s = floor((sqrt(2*apariciones+1/4)-1/2) + 1)
                    apariciones = floor(s*(s+1)//2)
                    if es_optimo(string, substring, apariciones, triangular):
                        reemplazos = 1
                    reemplazos -= 1

            else:

                while reemplazos > 0:

                    a, b = None, None
                    
                    string = mejorar(string, substring, a, b)

                    apariciones = contar(string, substring, False)

                    if es_optimo(string, substring, apariciones, False):
                        reemplazos = 1

                    reemplazos -= 1

        sys.stdout.write(str(apariciones) + '\n')