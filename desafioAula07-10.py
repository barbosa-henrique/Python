#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere US$ 1.00 = R$ 3.27
c = float(input('Informe o quanto dinheiro em R$ vc tem na carteira: '))
d = c / 3.27
print('Você pode comprar US$ {:.3}'.format(d))