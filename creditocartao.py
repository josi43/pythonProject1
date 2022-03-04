#comeca com 4,5,6
#n.lengh == 16
#contem digitos de 0-9
#grupos de 4 numeros, separados por -
#nao pode usar outro separador
#nao tem 4 ou mais digitos repetidos consecutivos
n='4253625879615786'

n_lista= list(n)


def check_comeco(inicio):
    if inicio[0]=='4' or inicio[0]=='5' or inicio[0]=='6':
        check=check_tamanho(n)
        return check
    else:
        return False

def check_tamanho(lista):
    if len(lista) == 16:
        chamada_digitos= check_digitos(n_lista)
        return chamada_digitos
    else:
        return False

def check_digitos(digitos):
    digitos_int = list(map(int,digitos))
        for
    return digitos_int


print(n)
print(n_lista)
if n_lista ==
print(check_comeco(n_lista))