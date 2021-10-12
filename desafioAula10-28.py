"""Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
O programa deverá escrever na tela se o usuário venceu ou perdeu"""
from random import randint
num1 = randint(0,5)
num2 = int(input('Em qual número estou pensando entre 0 e 5: '))
if num2 > 5:
    print('Você digitou um número diferente do esperado entre 0 e 5')
elif num2 == num1:
    print('Parabéns. Você acertou!')
else:
    print('Não foi dessa vez. Tente novamente mais tarde!\nO número que pensou foi {}'.format(num1))
print('Fim de jogo')