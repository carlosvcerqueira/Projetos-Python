'''import math
co = float(input('Tamanho cateto oposto: '))
ca = float(input('Tamanho cateto adjacente: '))
hipotenusa = math.hypot(co, ca)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))'''

co = float(input('Tamanho cateto oposto: '))
ca = float(input('Tamanho cateto adjacente: '))
hi = ((co**2 + ca**2))**(1/2)
print('O comprimento da hipotenusa é: {:.2f}'.format(hi))
