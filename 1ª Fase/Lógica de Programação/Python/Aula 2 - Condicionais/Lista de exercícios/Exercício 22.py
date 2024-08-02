while True:
    t = input(f'Quer passar a temperatura de Celsius pra Fahrenheit (CPF) ou de Fahrenheit pra Celsius (FPC)?').lower()
    if t=='cpf' or t=='fcp':
        break
    else:
        print(f'Escreve direito, idiota')
n = float(input(f'Qual a temperatura inicial?'))
if t=='cpf':
    print(f'Isso é o equivalente a {n*1.8+32} Fahrenheit')
else:
    print(f'Isso é o equivalente a {(n-32)/1.8} Celsius')