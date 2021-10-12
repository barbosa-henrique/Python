#Condições (parte 1)
#o IF no python tem que respeitar a identação correta com 'TAB'
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('='*3,'FIM','='*3)

print('Outra forma do IF')
print('carro novo'if tempo <= 3 else 'carro velho')
print('='*3,'FIM','='*3)