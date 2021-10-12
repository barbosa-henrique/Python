#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada
n = int(input('Informe um número inteiro '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('Número informado {}, dobro = a {}, triplo igual a {} e raiz igual a {}'.format(n, dobro, triplo, raiz))