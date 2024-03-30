#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = int(input('Digite um número: '))
soma = num
maior = num
menor = num
condi = 'Sim'
cont = 1

while condi[0] != 'N':
    num = int(input('Digite outro número: '))
    soma += num
    cont += 1

    if num > maior:
        maior = num
    elif menor > num:
        menor = num

    condi = str(input('\nDeseja continuar? ')).strip().upper()   
print('A média dos valores é {:.2f}, {} foi o maior valor digitado e {} o menor'.format(soma/cont, maior, menor)) 
