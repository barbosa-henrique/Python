"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo"""
r1 = float(input('Informe a reta 1 do triângulo: '))
r2 = float(input('Informe a reta 2 do triângulo: '))
r3 = float(input('Informe a reta 3 do triângulo: '))
if (r1 - r2) < r3 and (r1 + r2) > r3:
    print('É um triângulo válido')
else:
    print('Não é um triângulo válido')
print('FIM')