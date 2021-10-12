"""Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome"""
nome = str(input('Digite o nome de alguém: ')).strip()
nlista = nome.upper().split()
print('Esse nome contém "SILVA"? {}'.format('SILVA' in nlista))