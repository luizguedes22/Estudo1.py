peso = float ( input ( ' Digite o peso da pessoa: ' ) )
altura = float ( input ( ' Digite a altura da pessoa: ' ) )
IMC = peso / (altura ** 2)
print ( f' O IMC é {IMC:.1f} ' )
if IMC < 18.5:
    print ( ' Abaixo do peso ' )
elif IMC < 25:
    print ( ' Peso ideal ' )
elif IMC < 30:
    print ( ' Sobrepeso ' )
elif IMC < 40:
    print ( ' Obesidade ' )
else:
    print ( ' Obesidade Mórbida ' )
