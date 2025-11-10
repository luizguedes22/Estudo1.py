sidade = 0
midade = 0
mihomem = 0
nomevelho = ''
totmulher20 = 0
for p in range ( 1, 5 ):
    print ( f' Nome da {p}ª pessoa: ' )
    nome = str ( input ( ' Nome: ' ) ).strip()
    idade = int ( input ( ' Idade: ' ) )
    sexo = str ( input ( ' Sexo M/F: ' ) ).strip()
    sidade += idade
    if p == 1 and sexo in 'Mm':
        mihomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > mihomem:
        mihomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
midade = sidade / 4
print ( f' A média de idade do grupo é de {midade:.0f} anos ' )
print ( f' O homem mais velho tem {mihomem} anos e se chama {nomevelho} ' )
print ( f' Ao todo são {totmulher20} mulheres com menos de 20 anos ' )