#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Informe o salario do funcionario R$'))
novo = salario + (salario * 15/100)
print('O funcionario que ganhava {:.2f}R$ e com o aumento de 15%, seu salário atual ficou {:.2f}R$'.format(salario, novo))