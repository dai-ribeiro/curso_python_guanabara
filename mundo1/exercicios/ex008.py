# 008 - Escreva uma programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.

medida = float(input('Digite uma distância em metros: '))
cm = medida * 100
mm = medida * 1000

print('{} metros equivale a {:.0f} centimetros ou {:.0f} milimetros'.format(medida, cm, mm))
