'''n1=int(input('Digite o primeiro número:'))
n2=int(input('Digite o segundo número:'))
n3=int(input('Digite o terceiro número:'))
if n1 > n2 and n1 > n3:
    print(f'O número maior é: {n1}')
if n2 > n3 and n2 > n1:
    print(f'O número maior é: {n2}')
if n3 > n1 and n3 > n2:
    print(f'O número maior é: {n3}')
if n1 < n2 and n1 < n3:
    print(f'O menor número é: {n1}')
if n2 < n1 and n2 < n3:
    print(f'O menor número é: {n2}')
if n3 < n1 and n3 < n2:
    print(f'O menor número é: {n3}')'''

#outra forma:

n1=int(input('Digite o primeiro número:'))
n2=int(input('Digite o segundo número:'))
n3=int(input('Digite o terceiro número:'))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print (f'O maior número é: {maior}')
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor número é: {menor}')

