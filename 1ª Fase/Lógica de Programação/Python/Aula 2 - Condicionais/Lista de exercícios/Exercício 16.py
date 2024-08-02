while True:
    i = input(f'Você possui irmãos? Sim ou nao?').lower()
    if i=='sim':
        n = int(input(f'Quantos possui?'))
        print(f'LEGAL DEMAISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
        break
    elif i=='nao':
        print('Sorte a sua')
        break
    else:
        print(f'Escreve direito, idiota')