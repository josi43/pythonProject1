import copy
z = input()
lista = list(z)
def alphanum(z):
    a = copy.deepcopy(z)
    for i in range(len(a)):
        if a[0].isalnum():
            print(True)
            break
        else:
            a.pop(0)
            if a == []:
                print(False)
                break
def num(z):
    a = copy.deepcopy(z)
    for i in range(len(a)):
        if a[0].isalpha():
            print(True)
            break
        else:
            a.pop(0)
            if a == []:
                print(False)
                break
def digito(z):
    a = copy.deepcopy(z)
    for i in range(len(a)):
        if a[0].isdigit():
            print(True)
            break
        else:
            a.pop(0)
            if a == []:
                print(False)
                break
def lower(z):
    a = copy.deepcopy(z)
    for i in range(len(a)):
        if a[0].islower():
            print(True)
            break
        else:
            a.pop(0)
            if a == []:
                print(False)
                break
def uppper(z):
    a = copy.deepcopy(z)
    for i in range(len(a)):
        if a[0].isupper():
            print(True)
            break
        else:
            a.pop(0)
            if a == []:
                print(False)
                break
alphanum(lista)
num(lista)
digito(lista)
lower(lista)
uppper(lista)