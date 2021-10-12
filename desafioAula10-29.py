"""Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$ 7.00 para cada km acima do limite"""
vel = float(input('Informe a velocidade do carro: '))
if vel > 80:
    acima = vel - 80
    multa = acima * 7
    print('Você será multado.\nVocê excedeu o limite em {}\nA multa é no valor de R$ {}'.format(acima, multa))
else:
    abaixo = 80 - vel
    print('Parabéns. Você respeitou o limite de velocidade em {}'.format(abaixo))
print('-'*20)