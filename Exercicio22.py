# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

import time

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
time.sleep(3)
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
separação = nome.split()
print(f'Seu primeiro nome é {separação[0]} e este nome tem {len(separação[0])} letras.')