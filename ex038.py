from time import sleep
print('-=-'* 10)
print('ANALISADOR DE NÚMEROS')
print('-=-' * 10)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('ANALISANDO...')
sleep(3)
if n1 > n2:
    print('O primeiro valor é maior.')
elif n1 < n2:
    print('O segundo valor é maior.')
else:
    print('Os valores são iguais.')