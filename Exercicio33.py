#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
lista_numeros = []
for numeros in range (0,3):
    lista_numeros.append(float(input('Digite um número: ')))
print (f'\nO maior número foi {max(lista_numeros)}. E o menor número foi o {min(lista_numeros)}.')