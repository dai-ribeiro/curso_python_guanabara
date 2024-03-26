# Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Valor da reta 1: '))
r2 = float(input('Valor da reta 2: '))
r3 = float(input('Valor da reta 3: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print(f'Os segmentos acima formam um triângulo.')
else:
    print('Os segmentos acima não formam um triângulo.')