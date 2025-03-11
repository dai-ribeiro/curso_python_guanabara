# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que
#  tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

r1 = float(input('Valor da reta 1: '))
r2 = float(input('Valor da reta 2: '))
r3 = float(input('Valor da reta 3: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    if r1 == r2 and r2 == r3:
        print(f'Os segmentos acima formam um triângulo EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print(f'Os segmentos acima formam um triângulo ISÓSCELES.')
    elif r1 != r2 and r2 != r3:
        print(f'Os segmentos acima formam um triângulo ESCALENO.')
else:
    print('Os segmentos acima não formam um triângulo.')