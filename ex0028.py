import random
from time import sleep
num=random.randint(0,5)
dig=float(input('Digite o numero pensado:'))
print('\033[37mPROCESSANDO...\033[37m')
sleep(1)
if dig == num:
    print('Parabéns você acertou!!')
else:
    print(f'\033[31mPerdeu trouxa é {num}\033[m')
