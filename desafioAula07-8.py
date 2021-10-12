#Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros
n = float(input('Informe um valor em metros: '))
c = n * 100
m = n * 1000
print('Informado {} metros, em centimetros é {} e em milimetros é {}'.format(n,c,m))