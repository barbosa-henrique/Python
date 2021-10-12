"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao to_do (sem considerar espaços)
 Quantas letras tem o primeiro nome"""
nome = str(input('Digite um nome: '))
mai = nome.upper()
min = nome.lower()
ltodo = len(nome)-nome.count(' ')
l1 = nome.split()
print('Tudo maiúsculo: {}'.format(mai))
print('Tudo minúsculo: {}'.format(min))
print('Total de letras sem espaços: {}'.format(ltodo))
print('Primeiro nome é {}\nQuantidade de letras do primeiro nome é {}'.format(l1[0],len(l1[0])))
print(l1)