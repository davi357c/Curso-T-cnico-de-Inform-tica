while True:
    b = input(f'Qual bebida preferes? Refri (R), cerveja (C) ou água (A)?').upper()
    if b=='R':
        print('WOW! Melhor escolha!')
        break
    elif b=='C':
        print(f'És alcolatra?')
        break
    elif b=='A':
        print(f'Você é um ser estranho')
        break
    else:
        print(f'Escreve direito, idiota')