# Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Valor da reta 1: '))
r2 = float(input('Valor da reta 2: '))
r3 = float(input('Valor da reta 3: '))

if (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):
    print(f'As retas de tamanho {r1}, {r2} e {r3} podem formar um triângulo.')
else:
    print('As retas informadas não podem formar um triângulo.')