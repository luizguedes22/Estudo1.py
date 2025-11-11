num = int ( input ( ' Digite um número inteiro: ' ) )
print ( ''' Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL ''')
opção = int ( input ( ' Sua opção: ' ) )
if opção == 1:
    print ( f' O número {num} em binário fica {bin(num)[2:]} ' )
elif opção == 2:
    print ( f' O número {num} em octal fica {oct(num)[2:]} ' )
elif opção == 3:
    print ( f' O número {num} em hexadecimal fica {hex(num)[2:]} ' )
else:
    print ( ' Opção inválida, tente novamente! ' )
