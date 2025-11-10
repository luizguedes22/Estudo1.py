km=float(input('Digite os quilômetros rodados:'))
if km <= 200:
    valor= km*0.50
    print(f'Você irá pagar:R${valor:.2f}')
else:
    if km >= 200:
        valor2= km*0.45
    print(f'Você irá pagar:R${valor2:.2f}')