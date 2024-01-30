# 014 - Escreva um programa que converta uma temperatura digitada
# em Celcius e converta pra Farenheit

celcius = float(input('Informe a temperatura em Celcius: '))
farenheit = ((9 * celcius) / 5) + 32

print('A temperatura de {} ºC corresponde a {} ºF'.format(celcius, farenheit))
