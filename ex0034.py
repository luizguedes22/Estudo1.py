sal=float(input('\033[7mDigite seu salário: R$\033[m'))
aumento = sal + (sal*10/100)
aumento2 = sal + (sal*15/100)
if sal > 1250:
    print(f'Seu salário com aumento de 10% é: \033[32mR${aumento:.2f}')
else:
   if sal <= 1250:
        print(f'Seu salário com aumento de 15% é: \033[32mR${aumento2:.2f}')
