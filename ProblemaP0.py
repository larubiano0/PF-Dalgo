import sys


def es_optimo(string, substring, k):
    if substring[0] == substring[1]:
        if k == len(string)*(len(string)-1)//2:
            return True
        else:
            return False
    else:
        if k == (len(string)**2)//4:
            return True
        else:
            return False


def count(string, substring):
    '''
    Cuenta el número de veces que aparece substring en string
    '''
    apariciones = 0  # Numero total de apariciones de substring en string
    gsigns = 0  # Veces que aparece el primer caracter de substring en string
    a = substring[0]  # primer caracter de substring
    b = substring[1]  # segundo caracter de substring

    if a != b:  # En caso de que los caracteres del substring sean distintos

        i = 0

        while i < len(string):  # Itera sobre el string de izquierda a derecha

            if string[i] == a:

                gsigns += 1  # Incremente el número de apariciones del primer caracter de substring en string

            elif string[i] == b:

                apariciones += gsigns  # Si el segundo caracter de substring aparece en string, incremente el número de apariciones de substring en string

            i += 1

        return apariciones

    else:  # En caso de que los caracteres del substring sean iguales

        i = 0

        while i < len(string):  # Itera sobre el string de izquierda a derecha

            if string[i] == substring[0]:

                gsigns += 1  # Cuenta las veces que aparece el caracter en el string

            i += 1

        # Retorna el número triangular asociado al número de apariciones del caracter en string
        return gsigns*(gsigns-1)//2
    

if __name__ == "__main__":
    casos = int(sys.stdin.readline())  # Lee el número de casos
    for __ in range(casos):
        caso = sys.stdin.readline()
        string, substring, reemplazos = tuple(caso.split())
        reemplazos = int(reemplazos)

        apariciones = count(string, substring)
        sys.stdout.write(str(apariciones) + '\n')