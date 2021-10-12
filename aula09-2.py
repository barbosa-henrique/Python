#Analisando string
frase = 'Curso em Vídeo Python'
print(len(frase)) #len() indica o tamanho da string
print(frase.count('o')) #.count('caracter') - conta quantas vezes o caracater existe na string
print(frase.count('o',0,13)) #.count('caracter') - conta quantas vezes o caracater existe na string, da posição 0 até a posição 13
print(frase.find('deo')) #.find('caracter') - retorna em que momento começou a string passada como parâmetro
print(frase.find('android')) #.find('caracter') - se passar uma string que não existe, vai retornar '-1'
print('Curso' in frase) #'in' checa se a string existe dentro da variável
print(frase.replace('Python','Android')) #.replace substitui o trecho da string informado pelo outro
print(frase.upper()) #método .upper deixa o string em maiusculo
print(frase.lower()) #método .lower deixa o string em minusculo
print(frase.capitalize()) #método .capitalize deixa apenas a primeira posição do string em maiusculo
print(frase.title()) #método .title deixa apenas a primeira posição de cada palava da string em maiusculo

frase = '   Aprenda Python  '
print(frase)
print(frase.strip()) #Remove espaços adicionais
print(frase.rstrip()) #Remove espaços adicionais a direita
print(frase.lstrip()) #Remove espaços adicionais a esquerda
