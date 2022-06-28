#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import time
numero = int(input('Por favor digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print('O dobro de {} vale {}.'.format(numero,dobro))
time.sleep(1)
print('O triplo de {} vale {}.'.format(numero, triplo))
time.sleep(1)
print('A Raiz quadrada de {} vale {:.2f}.'.format(numero,raiz))