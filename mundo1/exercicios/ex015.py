# 015 - Escreva um programa que pergunte a quantida de km percoridos
# por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60
# por dia e R$ 0,15 por km rodado.

dias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos km foram percorridos? '))
total = (dias * 60) + (km * 0.15)

print('O valor a ser pago é R$ {:.2f}.'.format(total))
