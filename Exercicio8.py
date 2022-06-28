#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input('Digite uma quantidade em metros: '))
centimetros = metros*100
milimetros = metros*1000

print('{}m transformados em centimetros fica {}cm, e em milimetros fica {}mm'.format(metros,centimetros,milimetros))