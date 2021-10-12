#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import cos, sin, tan, radians
ang = float(input('Informe o ângulo: '))
cose = cos(radians(ang))
seno = sin(radians(ang))
tang = tan(radians(ang))
print('Coseno: {:.2f}\nSeno: {:.2f} \nTangente: {:.2f}'.format(cose, seno, tang))
