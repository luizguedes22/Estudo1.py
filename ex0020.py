'''import random

participantes = ['luiz','pedro', 'henrique', 'vitor', 'julio', 'joao', 'vanesso', 'bianco', 'fabiano', 'juliano']

for i in range(1, 5):
    sorteado=random.choice(participantes)
    participantes.remove(sorteado)
    print(f'O {i}º sorteado foi:{sorteado}')
    print('_'*30)'''

from random import shuffle
n1=str(input('Digite o primeiro nome:'))
n2=str(input('Digite o segundo nome:'))
n3=str(input('Digite o terceiro nome:'))
n4=str(input('Digite o quarto nome:'))
lista=[n1,n2,n3,n4]
shuffle(lista)
print('A ordem de alunos será:')
print(lista)