# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
# multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = float(input('Informe a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido de 80km/h')
    print(f'O carro foi multado. A multa será de R$ {multa:.2f}')
