# Desenvolva um programa que pergunte a distância de uma vigem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens
# até 200km e R$ 0,45 para viagens mais longas.

dist = float(input('Qual a distânia da viagem em km: '))

if dist <= 200:
    valor = dist * 0.5
else:
    valor = dist * 0.45

print(f'O valor da passagem será R$ {valor:.2f}')