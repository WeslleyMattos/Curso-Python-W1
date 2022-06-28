#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
import time

computador = randint(0,5)
print ('Olá! tente adivinhar o número que eu vou escolher entre 0 e 5! Vamos lá!' )
numero = int(input('Digite o número escolhido: '))
print ('PROCESSANDO...')
time.sleep(3)

if numero == computador:
    print(f'Parabéns você acertou!!!! O número era {computador}!')
else:
    print(f'Não foi dessa vez que você acertou, O número da vez era {computador}!')

print('===FIM===')

