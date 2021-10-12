"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
Ex: Ana Maria de Souza
primeiro: Ana
último: Souza"""
nome = str(input('Informe um nome: '))
lista = nome.split()
print('primeiro: {}'.format(lista[0]))
print('último: {}'.format(lista[len(lista)-1])) #"""O tamanho da lista (jose, maria, joão) é 3, mas ao passar o parâmetro lista[], tem que ser lista[2], posições 0 1 2"""