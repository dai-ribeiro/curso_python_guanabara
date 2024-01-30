# 017 - Faça uma programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo, calcule e mostre o
# comprimento da hipotenusa.

from math import sqrt, hypot

cat_op = float(input('Comprimento do cateto oposto: '))
cat_adj = float(input('Comprimento do cateto adjacente: '))
# hipotenusa = sqrt(cat_op ** 2 + cat_adj ** 2)
hipotenusa = hypot(cat_op, cat_adj)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
