b = 1
n = int(input(f'Escolha um número que deseja fatorar: '))
for v in range(n,1,-1):
    b*=v
    print(b)