# 020 - O mesmo professor do desafio anterior quer sortear a ordem
# de apresentação de trabalhos dos alunos. Faça um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 4: ')
aluno4 = input('Nome do aluno 4: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

ordem = random.choices(alunos, k=4)

print(f'A ordem de apresentação será: {ordem}')
