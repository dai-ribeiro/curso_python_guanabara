# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
# multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.

vel = int(input('Informe a velocidade do carro: '))

if vel > 80:
    multa = (vel - 80) * 7
    print(f'O carro foi multado. A multa será de R${multa}')