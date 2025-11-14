import datetime
atual = datetime.date.today().year
ano = int ( input ( ' Digite o ano de nascimento: ' ) )
idade = atual - ano
print ( f' A idade do atleta é {idade} ' )
if idade <= 9:
    print ( ' Você se encaixa na categoria MIRIM ' )
elif idade <= 14:
    print ( ' Você se encaixa na categoria INFANTIL ' )
elif idade <= 19:
    print ( ' Você se encaixa na categoria JUNIOR ' )
elif idade <= 25:
    print ( ' Você se encaixa na categoria SENIOR ' )
else:
    print ( ' Você se encaixa na categoria MASTER ' )
