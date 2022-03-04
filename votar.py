votaram={}
v=input('Deseja votar? s/n')
while v=='s':

    def verificar(nome):
        if votaram.get(nome):
            print('voce ja votou!')
        else:
            voto=input('deseja votar azul ou verde? ')
            votaram[nome]= True
    nome=input('qual seu nome ')
    verificar(nome)
    v = input('Deseja votar? s/n')
else:
    print('obrigado! ')
    print(votaram)
