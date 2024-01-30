# 013 - Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo sslário com 15% de aumento.

salario = float(input('Digite o salário: '))
novo_sal = salario * 1.15

print('Seu novo salário é R$ {:.2f}.'.format(novo_sal))