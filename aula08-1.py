#Importar biblioteca
#Exemplo - import.bebida - Mas isso lhe traria todas as bebidas (modo mais geral)
#Exemplo - from.bebida.import.cerveja - Traz um módulo específico da biblioteca que vc quer (modo mais específico)
#import.math (trazer toda a biblioteca)
#from.math.import.ceil (trazer da biblioteca o 'ceil', função para arredondar para cima, outras seriam: floor (arredondar para baixo), trunc, pow, sqrt, factorial)
import math #com importação geral
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {:.2f}, aproximadamente {} arredondarndo para cima'.format(num, raiz, math.ceil(raiz)))
print('A raiz de {} é igual a {:.2f}, aproximadamente {} arredondarndo para baixo'.format(num, raiz, math.floor(raiz)))


from math import sqrt, floor, ceil #com importação específica
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {:.2f}, aproximadamente {} arredondarndo para cima'.format(num, raiz, ceil(raiz)))
print('A raiz de {} é igual a {:.2f}, aproximadamente {} arredondarndo para baixo'.format(num, raiz, floor(raiz)))