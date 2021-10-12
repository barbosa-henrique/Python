n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('='*20)
print('A média é: {}'.format(m))
print('='*20)
if m >= 6:
    print('Aprovado')
else:
    print('Reprovado')
print('='*20)

print('Aprovado' if m>= 6 else 'Reprovado')