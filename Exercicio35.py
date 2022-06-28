#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
lado1 = float(input('Digite o primeiro número de três retas para que ele possa ser avaliado: '))
lado2 = float(input('Digite o segundo número de três retas para que ele possa ser avaliado: '))
lado3 = float(input('Digite o terceiro número para que ele possa ser avaliado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print ('As três retas informadas podem SIM criar um triângulo.')
else:
    print ('As retas informadas NÃO podem criar um triângulo.')