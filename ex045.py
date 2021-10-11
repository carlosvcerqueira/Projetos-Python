from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('PEDRA...')
sleep(0.7)
print('PAPEL...')
sleep(0.7)
print('TESOURA!!!')
sleep(1)
print('-=-'*7)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=-'*7)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador vence!')
    elif jogador == 2:
        print('Computador vence!')
    else:
        print('Jogada inválida, tente novamente!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('Computador vence!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador vence!')
    else:
        print('Jogada inválida, tente novamente!')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2:
        print('EMPATE!')
else:
        print('Jogada inválida, tente novamente!')