salario = float(input('Qual o seu salário? R$'))
if salario >= 1250:
    print('Com um aumento de 10% seu novo salário será R${:.2f}'.format(salario + (salario*0.10)))
else:
    print('Com um aumento de 15% seu novo salário será R${:.2f}'.format(salario + (salario * 0.15)))
