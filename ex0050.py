print ( ' Somente números pares contam na soma ' )
soma = 0
for c in range ( 0 , 6 ):
    numero = int ( input ( ' Digite um número inteiro: ' ) )
    if numero % 2 == 0:
        soma += numero
print ( f' a soma de todos os números pares é: {soma} ' )




