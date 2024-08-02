o = input(f'Escolha uma opção entre:\nSoma de 2 números. (S2N)\nDiferença entre 2 números (D2N)\nProduto entre 2 números. (P2N)\nDivisão entre 2 números. (DD2N)\n').lower()
while not o in ['s2n','d2n','p2n','dd2n']:
    o = input(f'Opção errada!\nEscolha uma opção entre:\nSoma de 2 números. (S2N)\nDiferença entre 2 números (D2N)\nProduto entre 2 números. (P2N)\nDivisão entre 2 números. (DD2N)\n').lower()
n1 = float(input('Escolha o primeiro número'))
n2 = float(input('Escolha o segundo número número'))
if o=='s2n':
    print(f'O resultado da soma é: {n1+n2}')
elif o=='d2n':
    print(f'O resultado da subtração é: {n1-n2}')
elif o=='p2n':
    print(f'O produto da multiplicação é: {n1*n2}')
else:
    while n2==0:
        print(f'O denominador não pode ser 0, escolha novamente')
        n1 = float(input('Escolha o primeiro número'))
        n2 = float(input('Escolha o segundo número número'))
    print(f'O resultado da divisão é: {n1/n2}')