# Escreva um programa que leia dois números inteiros e compare-os, mostrando n
# a tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O PRIMEIRO número informado ({num1}) é o maior.')
elif num2 > num1:
    print(f'O SEGUNDO número informado ({num2}) é o maior.')
else:
    print('Os números informados são IGUAIS.')
