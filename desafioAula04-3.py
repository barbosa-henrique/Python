print('========== DESAFIO 03 ==========')
#se vc fizer o input sem esse 'int', o tipo de entrada será considerada como um 'char' e não um number
n1 = int((input('Digite o valor 1: ')))
n2 = int((input('Digite o valor 2: ')))
soma = (n1 + n2)
print('A some vale: ',soma)
#outro modo de fazer o print
print('A some vale: {}'.format(soma))