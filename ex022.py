nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em caixa alta:', nome.upper())
print('Seu nome em mínusculas:', nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))








