from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Atletas nascidos em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade <= 9:
    print('Sua categoria é a MIRIM.')
elif idade <= 14:
    print('Sua categoria é a INFANTIL.')
elif idade <= 19:
    print('Sua categoria é a JÚNIOR.')
elif idade <= 25:
    print('Sua categoria é a SENIOR.')
else:
    print('Sua categoria é a MASTER.')