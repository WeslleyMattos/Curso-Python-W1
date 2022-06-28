#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido.

import random

lista = []
for nome in range (1,5):
    lista.append (input(f'Digite o nome do {nome}° aluno: '))
print(f'O aluno escolhido foi {random.choice(lista)}')
