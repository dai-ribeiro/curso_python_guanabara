# Crie um programa que faça o computador jogar
# Jokenpô com você.

import random

print(20 * '-', 'JOKENPÔ', 21 * '-')
print('[1] - Pedra')
print('[2] - Papel')
print('[3] - Tesoura')
print(50 * '-')

numero = random.randint(1, 3)

opcao_jogador = int(input('Escolha sua opção: '))

if opcao_jogador not in (1, 2, 3):
    print('Opção inválida!')

elif numero == 1:
    if opcao_jogador == 1:
        print('Jogue novamente. Ambos escolheram PEDRA.')
    elif opcao_jogador == 2:
        print('Você ganhou! PAPEL vence PEDRA.')
    elif opcao_jogador == 3:
        print('Você perdeu! PEDRA vence TESOURA.')

elif numero == 2:
    if opcao_jogador == 1:
        print('Você perdeu! PAPEL vence PEDRA.')
    elif opcao_jogador == 2:
        print('Jogue novamente. Ambos escolheram PAPEL.')
    elif opcao_jogador == 3:
        print('Você ganhou! TESOURA vence PAPEL.')

elif numero == 3:
    if opcao_jogador == 1:
        print('Você ganhou! PEDRA vence TESOURA.')
    elif opcao_jogador == 2:
        print('Você perdeu! TESOURA vence PAPEL.')
    elif opcao_jogador == 3:
        print('Jogue novamente. Ambos escolheram TESOURA.')

print()
