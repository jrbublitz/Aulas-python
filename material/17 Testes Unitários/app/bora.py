def soma(n1, n2):
    return n1 + n2


def raiz(n1):

    if not isinstance(n1, (int, float)):
        raise TypeError
    elif n1 < 0:
        raise ValueError

    return n1 ** 0.5


lista = [""]


def listadef(n):
    try:
        lista[n]
        return True
    except:
        return False


from random import randint


def muitas_strings(string):
    randint(1, 2)
    return string * randint(1, 100)


