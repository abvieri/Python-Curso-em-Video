# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
escolha = 0

while escolha != 5:
    print('Escolha o que quer fazer: ')
    escolha = int(input('\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n'))

    if escolha == 1:
        soma = num1 + num2
        print('\nA Soma dos número é: {}.'.format(soma))
    elif escolha == 2:
        mult = num1 * num2
        print('\nO Produto dos números é: {}'.format(mult))
    elif escolha == 3:
        print('\n{} é o maior número'.format(num1) if num1 > num2 else '\n{} é o maior número'.format(num2))
    elif escolha == 4:
        num1 = float(input('\nDigite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    elif escolha > 5 or escolha < 1:
        print('\nOpção inválida!')
print('Obrigado por usar nossos serviços!')