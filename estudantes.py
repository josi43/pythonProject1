estudante= []
notas= []
#pegar o nome e a nota numa turma de alunos e armazenar numa lista
# e imprimir os nomes dos estudantes com a segunda pior nota
#se tiver mais de um estudante com a pior nota, ordenar por ordem alfabetica

n_estudante=int(input(('')))
turma=[]
n=0
for i in range(n_estudante):
    e_nome = input('')
    nota = float(input(''))
    turma.insert(n,[nota,e_nome])
    n+=1
turma = sorted(turma)
n=0
"""def find_in_list_of_list(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            return (mylist.index(sub_list))
    raise ValueError("'{char}' is not in list".format(char = char))"""
for i in turma:
    notas.append(turma[n][0])
    estudante.append(turma[n][1])
    n+=1
notas=sorted(notas)
notas_org= list(set(notas))
if len(notas_org)>=2:
    minimo= min(notas_org)
    notas_org.remove(minimo)
    nota_final=min(notas_org)
    #segundo=(find_in_list_of_list(turma,nota_final))
    newlst=[ x for x in turma if nota_final in x]
    teste = len(newlst)
    n=0
    alfabetica =[]
    for x in range(teste):
        alfabetica.append(newlst[n][1])
        n+=1
    alf=sorted(alfabetica)
    for i in alf:
        print(i)
else:
    n=0
    for i in turma:
        print(turma[n][1])
        n+=1


