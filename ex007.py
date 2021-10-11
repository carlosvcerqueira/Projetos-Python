nome = input('Nome do aluno: ')
n1 = float(input('Nota primeira avaliação: '))
n2 = float(input('Nota segunda avaliação: '))
m = (n1+n2) / 2
print('A média final de {} é: {:.1f} '.format(nome, m))
