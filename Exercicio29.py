#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Diga quantos Km/Hora o carro estava: '))

if velocidade > 80:
     print(f'Você foi multado por estar acima do limite de 80Km/h! E terá que pagar uma multa de {(velocidade - 80) * 7}R$.')
     print('A multa foi calculada a 7R$ por cada Km acima do limite!')
else:
    print('Parabéns você estava dentro das normas de trânsito e respeitou o limite de 80Km/h!')

print('-=-' * 30)