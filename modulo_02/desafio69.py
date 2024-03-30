#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior = 0
homens = 0
mulheres = 0

while True:
    idade = int(input('\nDigite sua idade: '))
    sexo = str(input('Digite seu sexo: ')).strip().upper()
    cond = str(input('Deseja continuar cadastrando? ')).strip().upper()

    if idade > 18:
        maior += 1
    if sexo[0] == 'M':
        homens += 1
    if sexo[0] == 'F' and idade < 20:
        mulheres += 1

    if cond[0] == 'N':
        break
print(f'{maior} pessoas tem mais de 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{mulheres} mulheres tem menos de 20 anos')