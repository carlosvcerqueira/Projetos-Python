from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
cores = {'limpa': '\033[m', 'Vermelho': '\033[1:34:31m', 'Roxo': '\033[35:45m', 'amarelo': '\033[33:33m'}
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {}{}{} é BISSEXTO!'.format(cores['Vermelho'], ano, cores['limpa']))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))

