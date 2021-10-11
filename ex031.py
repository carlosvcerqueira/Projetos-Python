km = float(input('Quantos km você irá viajar? '))
if km <= 200:
    print('O valor da passagem é R${:.2f}'.format(km * 0.50))
else:
    print('O valor da passagem é R${:.2f}'.format(km * 0.45))