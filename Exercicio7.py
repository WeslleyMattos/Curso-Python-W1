#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input('Olá aluno digite seu nome: ')
nota1 = float(input('Digite sua nota de português: '))
nota2 = float(input('Digite agora sua nota de matemática: '))
media = (nota1 + nota2) /2
print('A média de suas notas são: {:.1f}'.format(media))
