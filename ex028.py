'''import random
n = (random.randint(0, 5))
print('Pensei em um número. Tente adivinhar!')
num = int(input('Qual o número? '))
if num == n:
    print('Como você sabia?!')
else:
    print('Não sabe porra nenhuma!')'''
from random import randint
computador = randint(0,5)
print('-=-' * 15)
print('Vou pensar em um número. Tente adivinhar...')
print('-=-' * 15)
jogador = int(input('Em que número estou pensando? '))
if computador == jogador:
    print('Você é brabão mesmo hein!')
else:
    print('Acerta nunca? Pensei no {}... HAHAHA'.format(computador))
print('-=-' * 15)
print('FIM DE JOGO!')
print('-=-' * 15)

