casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
prazo = int(input('Quantos anos de financiamento? '))
prestação = casa / (prazo * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(casa, prazo, prestação))
if prestação <= mínimo:
    print("Empréstimo APROVADO!")
else:
    print('Empréstimo NEGADO!')