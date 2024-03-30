#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite o número inteiro: '))
for cont in range(0,11):
    print('{} x {:2} = {}'.format(numero, cont , numero * cont))