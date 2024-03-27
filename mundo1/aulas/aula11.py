# Aula Extra: Cores no terminal

# ANSI - Escape Sequence
# \033[style;text;back m
# \033[0:33:44m

# Style:
# 0 - None
# 1 - Bold
# 4 - Underline
# 7 - Negative

# Text:
# 30 - branco
# 31 - vermelho
# 32 - verde
# 33 - amarelo
# 34 - azul
# 35 - magenta
# 36 - cian
# 37 - cinza

# Background:
# 40 - branco
# 41 - vermelho
# 42 - verde
# 43 - amarelo
# 44 - azul
# 45 - magenta
# 46 - cian
# 47 - cinza

print('Hello, world!')
print('\033[31mHello, world!')
print('\033[1;31;43mHello, world!\033[m')
print('\033[4;30;45mHello, world!\033[m')
print('\033[7;33mHello, world!\033[m')

# ------

a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m')

# ------

nome = 'Guanabara'

print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

# ------

nome = 'Guanabara'
cores = {'limpa': '\033[m', 
         'azul': '\033[34m', 
         'amarelo': '\033[33m', 
         'magenta': '\033[35m',
         'pretoebranco': '\033[7:30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['azul'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['magenta'], nome, cores['limpa']))