# 012 - Faça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.

preco_ant = float(input('Digite o valor do produto: '))
preco_nov = preco_ant * 0.95

print('O valor do produto com desconto de 5% é R$ {:.2f}.'.format(preco_nov))
