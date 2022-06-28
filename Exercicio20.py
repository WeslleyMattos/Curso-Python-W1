#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

lista = []
for nome in range (1,5) :
    lista.append(input(f'Digite o nome do {nome}° aluno: '))
    random.shuffle(lista)
print(f'A sequencia de alunos a se apresentar vai ser: {lista}')
