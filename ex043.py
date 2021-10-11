peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / altura ** 2
print('Com {}Kg e {}m o seu IMC é {:.1f}.'.format(peso, altura, imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('Você está com o PESO IDEAL.')
elif imc <= 30:
    print('Você está com SOBREPESO.')
elif imc <= 40:
    print('Você está OBESO.')
else:
    print('Você está com OBESIDADE MÓRBIDA.')
