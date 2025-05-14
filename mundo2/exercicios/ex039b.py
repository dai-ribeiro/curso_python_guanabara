# Faça um programa que leia o ano de nascimento de uma jovem e informe,
#  de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou 
# que passou do prazo.

from datetime import date

print()
ano_nascimento = int(input('Informe o ano de seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Faltam {18 - idade} anos para você se alistar.')
    ano = ano_atual + saldo
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você deveria ter se alistado há {idade - 18} anos.')
    ano = ano_atual - saldo
    print(f'Seu alistamento foi em {ano}.')
