i = int(input(f'Quantos anos você tem?'))
t = int(input(f'Qual o seu tempo de trabalho? (em anos)'))
if i>=65 or t>=30 or i>=60 and t>=25:
    print(f'Você pode se aposentar')
else:
    print(f'Você não pode se aposentar')