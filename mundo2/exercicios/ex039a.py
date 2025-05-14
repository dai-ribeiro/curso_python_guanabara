# Faça um programa que leia o ano de nascimento de uma jovem e informe,
#  de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou 
# que passou do prazo.

from datetime import datetime

ano_nascimento = int(input('Informe o ano de seu nascimento: '))
ano_atual = int(datetime.today().strftime('%Y'))
idade = ano_atual - ano_nascimento

if (idade) == 18:
    print('Está na hora de se alistar!')
elif (idade) < 18:
    print(f'Faltam {18 - idade} anos para você se alistar.', end='\n')
else:
    print(f'Já passaram {idade - 18} anos do tempo de se alistar.', end='\n')
