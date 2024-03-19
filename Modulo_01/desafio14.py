#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input('Digite a temperatura em graus Celsius: '))
print('A temperatura {}°C em graus Fahrenheit é de {:.1f}°F'.format(temperatura, temperatura*1.8 + 32))