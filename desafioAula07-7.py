#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
n1 = int(input('Informe a nota 1 do aluno: '))
n2 = int(input('Informe a nota 2 do aluno: '))
m = float((n1 + n2) / 2)
print('Nota 1 é {}, nota 2 é {} e a média é {}'.format(n1, n2, m))