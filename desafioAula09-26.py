"""Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra 'A'
Em que posição ela aparece pela primeira vez
Em que posição ela aparece a última vez"""
frase = str(input('Digite uma frase: ')).strip().upper()
print('Letra A aparece {} vezes na frase'.format(frase.count('A')))
print('Letra A aparece na posição {} pela primeira vez '.format(frase.find('A')))
print('Letra A aparece na posição {} pela última vez '.format(frase.rfind('A')))