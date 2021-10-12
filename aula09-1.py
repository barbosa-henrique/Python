#Trabalhando com string
frase = 'Curso em Video Python'
print(frase) #Imprime a variável frase
print(frase[9]) #Imprime a nona posição da variável 'frase' a primeira posição é 0
print(frase[9:15]) #Imprime da nona posição da variável 'frase' até décima quinta posição
print(frase[9:20:2]) #Imprime da nona posição da variável 'frase' até vigésima posição, pulando de 2 em 2 caracteres
print(frase[:15]) #antes do primeiro ':' vazio, indica que é da primeira posição da variável 'frase', até a posição 15
print(frase[5:]) #após o primeiro ':' vazio, indica que é da posição 5 da variável 'frase', até a última posição
print(frase[9::3]) #intervalo vazio entre '::' indica que é apartir da posição 9 da variável 'frase', até o final, pulando de 3 em 3 caracteres