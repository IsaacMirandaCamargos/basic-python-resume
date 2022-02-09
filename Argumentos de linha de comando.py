# A biblioteca sys permite que o python converse com o sistema operacional

import sys

# retorna o argumento passado ao sistema operacional para executar esse codigo
argumento = sys.argv

print(argumento)


# arg1  method // arg2 = n1 // arg3 = n2

def soma(n1, n2):
    return int(n1) + int(n2)


def sub(n1, n2):
    return int(n1) - int(n2)


if argumento[1] == "soma":
    resp = soma(argumento[2], argumento[3])
elif argumento[1] == "sub":
    resp = sub(argumento[2], argumento[3])

print(resp)
