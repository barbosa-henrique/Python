"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor"""
n1 = int(input('Informe o número 1: '))
n2 = int(input('Informe o número 2: '))
n3 = int(input('Informe o número 3: '))
menor = n1
maior = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Maior é: {}'.format(maior))
print('Menor é: {}'.format(menor))