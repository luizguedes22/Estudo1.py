velo=float(input('Digite a velocidade do carro:'))
if velo > 80:
    multa= (velo-80)*7
    print('Você foi multado em R$7,00 por km ultrapassado')
    print(f'Você irá pagar: \033[31;40m-R${multa:.2f}\033[m')
else:
    print('Boa viagem!!')