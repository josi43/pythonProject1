#fazer jogo da velha
print('Bem vindo ao jogo da velha, voce deve colocar o "x" ou "o" e selcionar a '
      'posicao desejada')
print('POSICOES')
print('1|2|3\n'
      '4|5|6\n'
      '7|8|9')
jogo={1:' ',2:' ',3:' ',
      4:' ',5:' ',6:' ',
      7:' ',8:' ',9:' '}
posicoes=[]
#recomeçar
def reco():
    n=input('deseja recomecar? s/n? ')
    if n == 's':
        print('POSICOES')
        print('1|2|3\n'
              '4|5|6\n'
              '7|8|9')
        jogar()
    else:
        print('fim de jogo')
#funcao para ver se alguem ganhou
def ganhar():
    if 'x' in jogo[1] and 'x' in jogo[2]and 'x'in jogo[3] or 'x' in jogo[4] and 'x' in jogo[5]and 'x'in jogo[6]or\
       'x' in jogo[7] and 'x' in jogo[8]and 'x'in jogo[9] or 'x' in jogo[1] and 'x' in jogo[4]and 'x'in jogo[7]or\
       'x' in jogo[2] and 'x' in jogo[5]and 'x'in jogo[8] or 'x' in jogo[3] and 'x' in jogo[6]and 'x'in jogo[9]or\
       'x' in jogo[1] and 'x' in jogo[5]and 'x'in jogo[9]or 'x' in jogo[3] and 'x' in jogo[5]and 'x'in jogo[7]:
        print('x ganhou')
        reco()
    elif'o' in jogo[1] and 'o' in jogo[2]and 'o'in jogo[3] or 'o' in jogo[4] and 'o' in jogo[5]and 'o'in jogo[6]or\
        'o' in jogo[7] and 'o' in jogo[8]and 'o'in jogo[9] or 'o' in jogo[1] and 'o' in jogo[4]and 'o'in jogo[7]or\
        'o' in jogo[2] and 'o' in jogo[5]and 'o'in jogo[8] or 'o' in jogo[3] and 'o' in jogo[6]and 'o'in jogo[9]or\
        'o' in jogo[1] and 'o' in jogo[5]and 'o'in jogo[9] or 'o' in jogo[3] and 'o' in jogo[5]and 'o'in jogo[7]:
        print('o ganhou')
        reco()
    else:
        jogar()
#colocar o x ou o
def imprimir(x,o):
    jogo[x]='x'
    jogo[o]='o'
    print(f'jogo   |  posicoes\n'
          f'{jogo[1]}|{jogo[2]}|{jogo[3]}  |  1|2|3\n'
          f'{jogo[4]}|{jogo[5]}|{jogo[6]}  |  4|5|6\n'
          f'{jogo[7]}|{jogo[8]}|{jogo[9]}  |  7|8|9')
    ganhar()
#funcao para o jogador colocar o input
def jogar():
    while True:
        jogador1 = int(input('em qual posicao voce deseja colocar o x? '))
        jogador2 = int(input('em qual posicao voce deseja colocar o O? '))
        if jogador1 in posicoes:
            print('posicao ja selecionada! Escolha outra opccao')
            jogar()
        elif jogador2 in posicoes or jogador2==jogador1:
            print('posicao ja selecionada! Escolha outra opccao')
            jogar()
        else:
            posicoes.append(jogador1)
            posicoes.append(jogador2)
            imprimir(jogador1,jogador2)
            return False
jogar()
