import random
de_novo='s'
while de_novo !='n':

    ppt=['pedra','papel','tesoura']
    jogador=input('pedra, papel ou tesoura? ').lower()
    computador=random.choice(ppt)
    while jogador not in ppt:
        jogador=input('pedra, papel ou tesoura? ').lower()
    print(f'O computador escolheu: {computador}')
    print(f'                         x')
    print(f'Voce escolheu:         {jogador}')
    if jogador == computador:
        print('empatou')
    elif jogador== 'pedra':
        if computador=='papel':
            print('voce perdeu!')
    elif computador=='tesoura':
            print('voce ganhou')
    elif jogador== 'papel':
        if computador=='tesoura':
            print('voce perdeu!')
        elif computador=='pedra':
            print('voce ganhou')
    elif jogador== 'tesoura':
        if computador=='pedra':
            print('voce perdeu!')
        elif computador=='papel':
            print('voce ganhou')
    de_novo=input('quer jogar de novo? s/n: ').lower()
print('Valeu por jogar!')
