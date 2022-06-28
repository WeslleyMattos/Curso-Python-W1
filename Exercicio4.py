#Faça um programa que leia algo pelo teclado e mostre na tela 
#o seu tipo primitivo e todas as informações possíveis sobre ele.

palavra = input('Digite algo: ')
print(f'Tipo primitivo é: {type(palavra)}')                                        
print(f'Só tem espaços? {palavra.isspace()}')                            
print(f'É decimal? {palavra.isdecimal()}')                                      
print(f'É númerico? {palavra.isnumeric()}')                                          
print(f'É alfabético? {palavra.isalpha()}')
print(f'É Algébrico? {palavra.isalnum()}')
print(f'Está em maiúsculos(las)? {palavra.isupper()}')
print(f'Está em minúsculas(los)? {palavra.islower()}')
print(f'Está capitalizada? {palavra.istitle()}')