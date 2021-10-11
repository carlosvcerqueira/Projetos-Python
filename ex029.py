velocidade = float(input('A que velocidade você passou? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi multado! O valor da multa é de R${:.2f}'.format(multa))
else:
    print('Tudo certo, boa viagem!')
