#Para imprimir um texto muito grande e várias linhas use três aspas duplas """texto"""
print("""AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC""")

frase = 'Curso em Vídeo Python'
print(frase.upper().count('O')) #combinou UPPER e COUNT. contar 'O' na frase depois de deixar tudo maiusculo

#uma string é imutável, suas posições não podem ser alteradas, a alteração é na variável
print('A variável frase tem valor de: ',frase.replace('Python','Android'), 'mas não mudamos o valor da variável')
print('A variável frase tem valor de: ',frase)
frase = frase.replace('Python','Android')
print('A variável frase agora tem valor de: ',frase)

dividido = frase.split() #dividido é uma variável do tipo lista
print(dividido)
print(dividido[0]) #primeira posicao da variavel dividido
print(dividido[0:2]) #primeira posicao da variavel dividido