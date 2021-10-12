#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número inteiro '))
nAnt = n - 1
nPos = n + 1
print('Número digitado {} \nNúmero antecessor {} \nNúmero sucessor {}'.format(n, nAnt, nPos))