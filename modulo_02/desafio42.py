#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))

if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    if  n1==n2==n3:
        print("Os segmentos podem formar um triângulo equilátero.")
    elif n1!=n2 and n1!=n3 and n2!=n3:
        print("Os segmentos podem formar um triângulo escaleno.")
    else:
        print("Os segmentos podem formar um triângulo isósceles.")
else:
    print('Os segmentos acima não podem formar um triângulo.')