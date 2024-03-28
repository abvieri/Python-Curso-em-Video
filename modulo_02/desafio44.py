#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

produto = float(input('Digite o valor do produto: '))
pagamento = str(input('Forma de pagamento: \n1- à vista dinheiro/cheque \n2- Cartão\n'))

if  pagamento == '1':
    print('O preço é R$ {:.2f}'.format(produto - (produto * 10 / 100)))
elif pagamento == '2':
    parcelas = int(input('Quantidade de parcelas: '))

    if parcelas == 1:
        print('O preço é R$ {:.2f}'.format(produto - (produto * 5 / 100)))
    elif  parcelas == 2:
        print('O preço é R$ {:.2f}'.format(produto))
    else:
        print('O preço é R$ {:.2f}, com juros de R$ {:.2f}.'.format((produto + (produto * 20 / 100)), produto))
else:
    print('Insira uma forma de pagamento válida')