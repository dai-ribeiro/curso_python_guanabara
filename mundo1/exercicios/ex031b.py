distancia = float(input('Qual a distânia da viagem em km: '))

valor = distancia * 0.5 if distancia <= 200 else distancia * 0.45   

print(f'O valor da passagem será R$ {valor:.2f}')