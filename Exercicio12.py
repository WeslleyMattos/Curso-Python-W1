#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com um desconto em porcentagem
import os

preço = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite o desconto do produto: '))
resultado = preço - (preço * desconto / 100)

print('O produto que custava R${:.2f}, na promoção com {}% de desconto, seu valor final vai ficar {:.2f}R$.'.format(preço, desconto, resultado))
input()
os.system('cls')