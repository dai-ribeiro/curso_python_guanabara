# Escreve um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange

num_sorteado = randrange(6)

num = int(input('Qual o número sorteado: '))

if num == num_sorteado:
    print('Você venceu!')
else:
    print(f'Você perdeu! O número sorteado foi {num_sorteado}.')