frase=str(input('Digite uma frase:')).upper().strip()
print(f'a frase tem: {frase.count('A')} letras A')
print(f'A posição que ela aparece primeirpo é: {frase.find('A')+1}')
print(f'A posição que ela aparece a ultima vez é: {frase.rfind('A')+1}')