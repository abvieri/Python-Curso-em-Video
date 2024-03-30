#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
while sexo not in 'Mf':
    if sexo  != 'M' and sexo != 'F' and sexo != '':
        sexo = input('Digite apenas M para Masculino e F para Feminino: ')
print('Obrigado, sexo registrado com sucesso')
        