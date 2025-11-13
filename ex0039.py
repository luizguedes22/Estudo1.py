import datetime
ano = datetime.date.today().year
nascimento = int ( input ( ' Digite o ano de nascimento: ' ) )
idade = ano - nascimento
if idade == 18:
    print ( ' É hora de se alistar! ' )
elif idade > 18:
    saldo = idade - 18
    print ( f' Já passou da hora de se alistar, você atrasou {saldo} anos! ' )
    print ( f' Você deveria ter se alistado em {ano-saldo} ' )
elif idade < 18:
    saldo = 18 - idade
    print ( f' Ainda faltam {saldo} ano/s ' )
    print ( f' Você terá de se alistar em {ano+saldo} ' )
