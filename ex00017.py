'''from math import sqrt
valor1=float(input('Digite o valor do "CO":'))
valor2=float(input('Digite o valor do "CA":'))
resultado=(valor1**2)+(valor2**2)
igual=sqrt(resultado)
print(f'O comprimeneto da hipotenusa é igual a:{igual:.2f}')'''

from math import hypot
co=float(input('Digite o cateto oposto:'))
ca=float(input('Digite o cateto adjacente:'))
hi= hypot(co,ca)
print(f'A hipotenusa vai medir:{hi:.2f}')
