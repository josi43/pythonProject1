marks_key={}
nomes=[]
pontos=[]
try:
    estudantes=int(input(''))
except ValueError:
    print('')
else:
    def nome_aluno(n):
        for i in range(n):
            strs = input("")
            d = (strs.split())
            d_nome=d[0]
            d_numeros=d[1:]
            d_numeros_int = []
            for i in d_numeros:
                d_numeros_int.append((float(i)))

            dicio={d_nome:d_numeros_int}
            marks_key.update(dicio)

    def sum(list):
        if list == []:
            return 0
        return list[0] + sum(list[1:])
    def consulta():
        nome=input('')
        if nome in marks_key:
            consult=(marks_key[nome])
            media=sum(consult)/3
            media = "{:.2f}".format(media)
            print(media)
        else:
            print('esse nome nao esta aqui')
    if estudantes>=1:
        nome_aluno(estudantes)

    consulta()

