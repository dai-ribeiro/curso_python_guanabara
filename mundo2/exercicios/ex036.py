# Escreva um programa para aprovar o empréstimo bancário para compra de uma
# casa. O programa vai perguntar o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
# salário ou então o empréstimo será negado.

print(50 * '-')
print(14 * ' ', 'ANÁLISE DE CRÉDITO')
print(50 * '-')

valor_imovel = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o seu salário? R$ '))
prazo = int(input('Em quantos anos pretende pagar? '))

prazo_meses = prazo * 12
prestacao = valor_imovel / prazo_meses
limite_prestacao = salario * 0.3

if prestacao > limite_prestacao:
    print('Empréstimo NEGADO!')
    print(f'O valor da prestação R$ {prestacao:.2f} ultrapassa 30% do seu salário.')
else:
    print('Empréstimo CONCEDIDO!')
    print(f'Você irá pagar {prazo_meses} prestações de R$ {prestacao:.2f}.')
