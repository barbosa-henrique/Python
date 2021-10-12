#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhidos
from random import choice
a1 = str(input('Informe aluno 1: '))
a2 = str(input('Informe aluno 2: '))
a3 = str(input('Informe aluno 3: '))
a4 = str(input('Informe aluno 4: '))
lista = [a1, a2, a3, a4]
sor = choice(lista)
print('Aluno escolhido foi {} '.format(sor))