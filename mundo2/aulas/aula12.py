nome = str(input('Qual é seu nome? '))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Paulo' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssia Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
