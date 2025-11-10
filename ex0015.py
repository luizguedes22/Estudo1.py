dias=float(input('Digite os dias de aluguel:'))
km=float(input('Digite quantos km rodados:'))
valor= (dias*60)+(km*0.15)
print(f'O valor a ser pago é de:R${valor:.2f}')