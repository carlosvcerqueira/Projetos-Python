import math
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
# Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o menor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))
