# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
import os

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
tinta = area / 2
print('Sua parede tem {}m², e você vai precisar de {}L de tinta para pintar essa área.'.format(tinta, area))

input()
os.system('cls')