#Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for cont in range(1, 51):
    print(cont if cont%2 == 0 else " ", end="")