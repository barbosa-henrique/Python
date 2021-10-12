#Divisão de string
frase = 'Curso em Video Python'
frase = frase.split() #Divide um string em uma lista, onde cada elemente é dividido pelo caracter ' ' espaço
print(frase)

frase = '-'.join(frase) #junta uma lista com base no caracter informado antes do join
print(frase)