#Operadores aritméticos
# + adição
# - subtração
# * multilicação
# / divisão
# ** potência
# // divisão inteira
# % resto da divisão

op1 = int(input('Valor do operando 1: '))
op2 = int(input('Valor do operando 2: '))
adicao = op1 + op2
subtracao = op1 - op2
multiplicacao = op1 * op2
divisao = op1 / op2
potencia = op1 ** op2
div_inteira = op1 // op2
resto_div = op1 % op2
print('Soma de {} e {} é igual a {}'.format(op1, op2, adicao))
print('Subtracao de {} e {} é igual a {}'.format(op1, op2, subtracao))
print('Multiplicacao de {} por {} é igual a {}'.format(op1, op2, multiplicacao))
print('Divisao de {} por {} é igual a {}'.format(op1, op2, divisao))
print('Potencia de {} elevado a {} é igual a {}'.format(op1, op2, potencia))
print('Divisao inteira de {} por {} é igual a {}'.format(op1, op2, div_inteira))
print('Resto da divisao de {} por {} é igual a {}'.format(op1, op2, resto_div))

#ordem de precedência
# 1 _ ()
# 2 _ **
# 3 _ * / // %
# 4 _ + -