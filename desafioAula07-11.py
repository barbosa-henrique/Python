#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
larg = float(input('Informe a largura: '))
alt = float(input('Informe a altura: '))
area = larg * alt
qt = area / 2
print('Largura {}\n'
      'Altura {}\n'
      'Area calculada {}\n'
      'Quantidade de tinta necessária {}'.format(larg, alt, area, qt))