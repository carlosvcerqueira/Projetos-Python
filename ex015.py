km = float(input('Quantos km foram percorridos com o carro?: '))
dias = int(input('Por quantos dias o carro foi alugado?: '))
v = (dias * 60) + (km * 0.15)
print('Total a pagar é R${:.2f} '.format(v))
