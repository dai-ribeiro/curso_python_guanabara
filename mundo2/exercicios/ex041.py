# A Confederação Nacional de Natação precisa de um programa que leia o ano de
#  nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import datetime

ano_atual = int(datetime.now().strftime('%Y'))

ano_nascimento = int(input('Informe seu ano de nascimento: '))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'Idade: {idade}')
    print('Categoria: MIRIM')
elif idade <= 14:
    print(f'Idade: {idade}')
    print('Categoria: INFANTIL')
elif idade <= 19:
    print(f'Idade: {idade}')
    print('Categoria: JUNIOR')
elif idade <= 20:
    print(f'Idade: {idade}')
    print('Categoria: SÊNIOR')
else:
    print(f'Idade: {idade}')
    print('Categoria: MASTER')
