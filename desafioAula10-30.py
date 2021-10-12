"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR"""
num = int(input('Informe um número inteiro: '))
if num % 2 == 0:
    print('Número {} é PAR'.format(num))
else:
    print('Número {} é IMPAR'.format(num))
print('-'*20,'FIM','-'*20)