print('-=-' * 15)
print('Analisador de triangulos!')
print('-=-' * 15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os segmentos acima PODEM FORMAR tríangulo!')
else:
    print('Os segmentos acima NÃO PODEM formar tríangulo!')
