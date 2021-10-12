#Cire um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
#Exemplo: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6
from math import trunc
n = float(input('Informe um número: '))
print('O número {0} tem a parte inteira igual a {1}'.format(n,trunc(n)))