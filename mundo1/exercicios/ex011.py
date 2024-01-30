# 011 - Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
area = largura * altura
tinta = area / 2

print('Será necessário {:.2f} litros de tinta para pintar uma parede de {:.2f}m2.'.format(tinta, area))
