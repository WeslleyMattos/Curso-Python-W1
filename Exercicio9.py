#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número para ver sua tabuada: '))
print ('---' * 4)
for contador in range(1,11):
    print('{} x {:2} = {}'.format(num, contador, num*contador))
print ('----' * 3)