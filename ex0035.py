r1=float(input('Digite a medida da primeira reta:'))
r2=float(input('Digite a medida da segunda reta:'))
r3=float(input('Digite a medida da terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triângulo!')
else:
    print('Não forma um triângulo :(')