nome = str(input('Qual seu nome? '))
teste = str(input('Hoje vai chover? '))
if teste == 'Sim':
    print('Então leve um guarda-chuva')
print('Bom dia {}'.format(nome))
#Essa linha já está fora do IF. IF só executa o que está dentro da identação com um TAB #Só vai escrever a mensagem do guarda-chuva, se a resposta da pergunta for 'sim'
#Comandos colados no lado esquerdo, sempre são executados