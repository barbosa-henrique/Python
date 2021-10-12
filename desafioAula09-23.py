"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
EX:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1"""
num = int(input('Informe um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))

"""Usar esse método, pq ainda não fizemos uma validação através de uma condição IF, para se certificar que realmente foram digitados apenas 4 ou menos casas
caso digitem mais ou menos, não dará problema no programa"""