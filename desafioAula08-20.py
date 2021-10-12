#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quadtro alunos e mostre a ordem sorteada
from random import shuffle, sample
a1 = str(input('Informe aluno 1: '))
a2 = str(input('Informe aluno 2: '))
a3 = str(input('Informe aluno 3: '))
a4 = str(input('Informe aluno 4: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('Ordem de sorteio: {}'.format(lista))

#outra forma que fiz, antes de ver o video

ordem = sample(lista,4)
print('Ordem de sorteio: {}'.format(ordem))