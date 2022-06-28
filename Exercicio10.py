#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 4.72 #Sdds
print ('Com R${:.2f} você pode comprar US${:.2f}'.format(real,dolar))