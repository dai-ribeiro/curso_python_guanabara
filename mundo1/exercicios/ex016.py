# 016 - Crie um programa que leia um número real qualquer pelo
# teclado e mostre na tela a sua porção inteira. Ex: Digite um
# número: 6.127. O número 6.127 tem a parte intera 6.

from math import modf, trunc

num = float(input('Digite um número real: '))

print('O número {} tem a parte inteira {}'.format(num, int(modf(num)[1])))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
print('O número {} tem a parte inteira {}'.format(num, int(num)))
