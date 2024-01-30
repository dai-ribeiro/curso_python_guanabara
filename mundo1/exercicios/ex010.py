# 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = 3,27

real = float(input('Qual valor deseja converter? R$ '))
dolar = real / 3.27
print('O valor R${:.2f} equivale a ${:.2f}'.format(real, dolar))
