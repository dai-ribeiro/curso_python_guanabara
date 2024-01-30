# 018 - Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Ângulo: '))
rad = math.radians(ang)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f'O ângulo {ang} tem seno {round(seno, 2)}, cosseno {round(cosseno, 2)} e tangente {round(tangente, 2)}')
