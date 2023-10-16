#import random

#n1 = input ('Digite seu nome: ')
#n2 = input ('Digite seu nome: ')
#n3 = input ('Digite seu nome: ')
#n4 = input ('Digite seu nome: ')

#lista = [n1, n2, n3, n4]
#sorteado = random.choice (lista)

#print ('O aluno escolhido foi: {}'.format(sorteado))

from random import choice

alunos = input('Escreva o nome dos alunos separados por vírgula: ').split(", ")
print('O aluno escolhido foi: {}'.format(choice(alunos)))
