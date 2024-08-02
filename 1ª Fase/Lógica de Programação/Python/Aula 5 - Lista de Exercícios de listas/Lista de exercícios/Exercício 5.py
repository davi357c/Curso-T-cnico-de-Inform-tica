list_all, list_par, list_impar = [], [], []
for v in range(20):
    number = int(input(f'Digite um número inteiro: '))
    list_all.append(number)
    if number % 2 == 1:
        list_impar.append(number)
    elif number % 2 == 0:
        list_par.append(number)
print(f'Lista total: {list_all}\nLista ímpar: {list_impar}\nLista par: {list_par}')
