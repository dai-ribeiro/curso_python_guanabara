# 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# ** O nome com todas as letras maiúsculas
# ** O nome com todas as letras minúsculas
# ** Quantas letras no total (sem considerar espaços)
# ** Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Maiúscula: {nome.upper()}')
print(f'Minúscula: {nome.lower()}')
print(f'Total de letras: {len(nome) - nome.count(" ")}')
print(f'Total letras primeiro nome: {len(nome.split()[0])}')
# print(f'Total letras primeiro nome: {nome.find(" ")}')

