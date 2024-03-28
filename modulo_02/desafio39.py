#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input("Digite a idade: "))
if idade < 18:
    print('Ainda Faltam {} anos para você se alistar'.format(18 - idade))
elif idade == 18:
    print('Está na hora do seu alistamento')
else:
    print('Já passaram {} anos do seu alistamento, se aliste o quanto antes!'.format(idade - 18))