"""Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO"""
ano = int(input('Informe um ano: '))
if ano % 4 == 0:
    print('Ano BISSEXTO')
else:
    print('Não é BISSEXTO')
