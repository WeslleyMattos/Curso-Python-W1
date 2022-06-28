#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
import math

numero = float(input('Digite um número com ponto: '))
print('O número {} tem a parte inteira {}'.format(numero, math.floor(numero)))