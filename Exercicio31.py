#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = int(input('Digite a distância da viagem percorrida em Km: '))
if distancia <= 200:
    viagem_pequena = (distancia * 0.50)
    print (f'O valor da passagem para {distancia}Km fica: R${viagem_pequena:.2f}')
else:
    viagem_longa = (distancia * 0.45)
    print (f'O valor da passagem para {distancia}Km fica: R${viagem_longa:.2f}')
