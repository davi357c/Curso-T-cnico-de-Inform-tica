n1 = float(input(f'Escolha um número'))
n2 = float(input(f'Escolha outro número'))
while True:
    o = input(f'Quer fazer multiplicação (M) ou divisão (D)?').lower()
    if o=='m':
        print(f'A resposta é: {n1*n2}')
        break
    elif o=='d':
        print(f'A resposta é: {n1/n2}')
        break
    else:
        print(f'Escreve direito, idiota')