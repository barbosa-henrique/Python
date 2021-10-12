"""Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0.50 po km para viagens de até 200km e R$ 0.45 para viagens mais longas"""
dist = float(input('Informe a distância da viagem: '))
if dist > 200:
    valor = dist * 0.45
    print('Valor da viagem é: {}'.format(valor))
else:
    valor = dist * 0.50
    print('Valor da viagem é: {}'.format(valor))
print('Boa viagem')