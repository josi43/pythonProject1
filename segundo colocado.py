lista=[]
tamanho=int(input(''))

b = input('' )
a = b.split(' ')
a = list(map(int,a))
n = 0
for i in range(tamanho):
    lista.insert(n,a[n])
    n+=1
lista = sorted(lista)
lista_unica=list(set(lista))
novo_tamanho=len(lista_unica)
print(lista_unica[novo_tamanho-2])

