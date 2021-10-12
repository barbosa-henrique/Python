"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'."""
cidade = str(input('Informe uma cidade: ')).strip()
nome1 = cidade.upper().split()
print('Cidade começa com "SANTO"?: {}'.format('SANTO' in nome1[0]))