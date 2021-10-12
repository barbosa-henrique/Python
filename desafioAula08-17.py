#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente '))
hi = hypot(co,ca)
print('O comprimento da hipotenusa é {}'.format(hi))