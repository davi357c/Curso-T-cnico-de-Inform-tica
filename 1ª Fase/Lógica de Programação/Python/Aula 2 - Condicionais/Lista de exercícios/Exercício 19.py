n1 = float(input(f'Escolha um número'))
n2 = float(input(f'Escolha outro número'))
while True:
    o = input(f'Quer fazer adição (A) ou subtração (S)?').lower()
    if o=='a':
        print(f'A resposta é: {n1+n2}')
        break
    elif o=='s':
        print(f'A resposta é: {n1-n2}')
        break
    else:
        print(f'Escreve direito, idiota')