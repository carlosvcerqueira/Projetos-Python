from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {}, tem {} anos em {}.'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    alistamento = atual + saldo
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Você irá se alistar em {}.'.format(alistamento))
elif idade > 18:
    saldo = idade - 18
    alistamento = atual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Você deveria ter se alistado em {}.'.format(alistamento))


