n1 = float ( input ( ' Digite a primeira nota: ' ) )
n2 = float ( input ( ' Digite a segunda nota: ' ) )
média = (n1 + n2) / 2
print ( f' Sua média é: {média:.1f} ' )
if média <= 5.0:
    print ( 'REPROVADO!' )
elif média < 6.9:
    print ( 'RECUPERAÇÃO!' )
elif média >= 7.0:
    print ( 'APROVADO!' )
