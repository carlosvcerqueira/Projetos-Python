n = float(input('Quanto dinheiro você tem na carteira?: R$'))
d = n / 5.61
e = n / 6.57
print('Com {:.2f} você consegue comprar US${:.2f} e EU${:.2f}.'.format(n, d, e))
