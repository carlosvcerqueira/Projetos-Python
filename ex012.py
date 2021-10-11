preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('Na liquidação, o produto que custava R${:.2f} com 5% de desconto irá custar R${:.2f}.'.format(preço, novo))

