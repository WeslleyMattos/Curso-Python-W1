#Faça um programa que leia um número de 0 a 9999 
# e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número entre 0 e 9999: '))
unidade = numero // 1 % 10 #pega o numero divide por 10 e pega o resto da divisao que seria minha unidade
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Analisando o número {numero}')
print(f'Unidade: {unidade} \nDezena: {dezena} \nCentena: {centena} \nMilhar: {milhar}')