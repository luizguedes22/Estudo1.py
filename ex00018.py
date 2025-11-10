'''import math
angulo = int(input('Digite o ângulo:'))
seno= math.sin(math.radians(angulo))
print(f'O valor do seno é: {seno:.2f}')
cos= math.cos(math.radians(angulo))
print(f'O valor do cosseno é: {cos:.2f}')
tang= math.tan(math.radians(angulo))
print(f'O valor da tangente é: {tang:.2f}')'''

from math import radians, sin, cos, tan

angulo=float(input('Digite o ângulo:'))
sen=radians(angulo)
cose=radians(angulo)
tang=radians(angulo)
print(f'O valor de seno é: {sin(sen):.2f}')
print(f'O valor do cosseno é: {cos(cose):.2f}')
print(f'O valor da tangente é: {tan(tang):.2f}')