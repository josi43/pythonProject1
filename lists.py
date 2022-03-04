# numero de comandos
N = int(input(''))
list=[]
#colocar valor no indice solicitado
def inserir(z):
    com_z,val_z, index_z= z.split(' ')
    val_z = int(val_z)
    index_z =int(index_z)
    list.insert(val_z, index_z )
#deletar a primeira ocorrencia do int(e)
def remover(z):
    com_z, val_z=z.split(' ')
    val_z = int(val_z)
    if val_z  in list:
        list.remove(val_z)
    else:
        pass
#inserir e no final da lista
def add_final(z):
    com_z, val_z = z.split(' ')
    val_z = int(val_z)
    list.append(val_z)
#organizar a list
def org_list(z):
    list.sort()
#tirar o ultimo elemento da lista
def rem_final():
    list.pop()
#reverter a lista
def revert():
    list.reverse()
    return list
for i in range(N):
    comando=input('')
    #chamada de funcoes
    if 'insert' in comando:
        inserir(comando)
    elif 'remove'in comando:
        remover(comando)
    elif 'append' in comando:
        add_final(comando)
    elif 'sort' in comando:
        org_list(comando)
    elif 'pop' in comando:
        rem_final()
    elif 'reverse' in comando:
        revert()
    elif 'print' in comando:
        print(list)
    else:
        pass