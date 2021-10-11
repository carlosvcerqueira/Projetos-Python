salário = float(input('Qual o sálario do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Com o aumento de 15%, o salário passaria de R${:.2f} para R${:.2f}.'.format(salário, novo))
