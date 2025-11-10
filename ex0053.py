frase = str ( input ( ' Digite uma frase: ' ) ).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print ( ' Temos um palindromo! ' )
else:
    print ( ' Essa frase não é um palindromo ' )


