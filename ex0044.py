print ( f' {'Lojas Guedes':=^40} ' )
preco = float ( input ( ' Preço das compras: R$ ' ) )
print ( ''' Formas De Pagamento 
[ 1 ] À  vista no dinheiro/cheque 
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão (com juros) ''')
opcao = int ( input ( ' Qual a opção: ' ) )
if opcao == 1:
    total = preco - ( preco * 10 / 100 )
    print ( total )
elif opcao == 2:
    total = preco - ( preco * 5 / 100 )
    print ( total )
elif opcao == 3:
    total = preco
    parcela = total / 2
    print ( f' Sua compra será parcelada em 2 vezes de R${parcela:.2f} ' )
elif opcao == 4:
    total = preco + ( preco * 20 / 100 )
    totparcelas = int ( input ( ' Quantas parcelas: ' ) )
    parcela = total / totparcelas
    print ( f' Sua compra será parcelada em {totparcelas}x de R${parcela:.2f} com juros ' )
else:
    total = 0
    print ( ' \033[31m Erro de digitação! \033[m ' )
print ( f' Sua compra de R${preco:.2f} vai custar R${total:.2f} no final ' )
