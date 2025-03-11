# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print(50 * '-')
print('FORMAS DE PAGAMENTO')
print('[1] - À visa no dinheiro/cheque')
print('[2] - À visa no cartão')
print('[3] - Em 2x no cartão')
print('[4] - Em 3x ou mais no cartão')
print(50 * '-')

forma_pgto = int(input('Selecione a forma de pagamento desejada: '))
valor_produto = float(input('Informe o valor de produto: R$ '))

print(50 * '-')

if forma_pgto == 1:
    valor_pagar = valor_produto * 0.9
    print(f'Valor a ser pago: R$ {valor_pagar:.2f}')
elif forma_pgto == 2:
    valor_pagar = valor_produto * 0.95
    print(f'Valor a ser pago: R$ {valor_pagar:.2f}')
elif forma_pgto == 3:
    print(f'Valor a ser pago: R$ {valor_produto:.2f}')
elif forma_pgto == 4:
    valor_pagar = valor_produto * 1.2
    print(f'Valor a ser pago: R$ {valor_pagar:.2f}')
else:
    print('Opção de pagamento inválida!')

print(50 * '-')
