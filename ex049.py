num = int(input('Digite um número para ver sua tabuada: '))
for n in range(0, 11):
    print('{} x {:2} = {}'.format(num, n, num*n))