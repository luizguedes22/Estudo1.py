t1 = int ( input ( ' Primeiro termo: ' ) )
ra = int ( input ( ' Razão: ' ) )
decimo = t1 + ( 11 - 1 ) * ra
for c in range ( t1, decimo, ra, ):
    print (c)