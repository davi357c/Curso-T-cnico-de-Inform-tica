while True:
    g = input(f'Qual seu gênero? (M) ou (F)?').lower()
    if g=='m' or g=='f':
        a = float(input(f'Qual a sua altura?'))
        if g=='m':
            print(f'Seu peso ideal é de {(72.7*a)-58}')
        elif g=='f':
            print(f'Seu peso ideal é de {(62.1*a)-44.7}')        
        break
    else:
        print(f'Escreve direito, idiota')
