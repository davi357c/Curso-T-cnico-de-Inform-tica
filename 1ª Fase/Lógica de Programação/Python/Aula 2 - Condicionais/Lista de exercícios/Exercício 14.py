while True:
    sexualidade = input(f'Você é gay? Sim ou nao?').lower()   
    if sexualidade=='sim':
        print(f'Você acertou!!')
        break
    elif sexualidade=='nao':
        print(f'Você errou Grrr!')
        break
    else:
        print(f'Escreve direito idiota')