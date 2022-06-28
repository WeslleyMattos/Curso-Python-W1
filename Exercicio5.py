#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Por favor digite um número: '))
antecessor = (numero - 1)
sucessor = (numero + 1)

print('Sendo o número {}, o antecessor dele fica {} e o sucessor {})'.format(numero,antecessor,sucessor))