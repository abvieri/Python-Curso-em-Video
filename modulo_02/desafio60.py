#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Digite um número: '))
cont = num
fatorial = num

print('Calculando {}! = {} x '.format(num, num), end='')
while cont != 1:
    cont = cont - 1
    fatorial = (cont)*fatorial

    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
print('{}'.format(fatorial))
