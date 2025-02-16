# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 - para binário
# 2 - para octal
# 3 - para hexadecimal

numero = int(input('Digite um número: '))
print('''
Selecione a base para conversão:
    [ 1 ] Binário
    [ 2 ] Octal
    [ 3 ] Hexadecimal
''')
base = int(input('Opção escolhida: '))

if base == 1:
    bin_numero = bin(numero)
    print(f'O número {numero} em binário é {bin_numero[2:]}.')
elif base == 2:
    octal_numero = oct(numero)
    print(f'O número {numero} em octal é {octal_numero[2:]}.')
elif base == 3:
    hexa_numero = hex(numero)
    print(f'O número {numero} em hexadecimal é {hexa_numero[2:]}.')
else:
    print('Opção inválida!')
