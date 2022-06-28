#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = float(input('Digite um número aleatório: '))
resultado = numero % 2 #qualquer numero par vai ser igual a 0 e impar igual 1 se fizer o resto da divisao por 2
if resultado == 0:
    print('O número escolhido é PAR!')
else:
    print('O número escolhido é IMPAR!')