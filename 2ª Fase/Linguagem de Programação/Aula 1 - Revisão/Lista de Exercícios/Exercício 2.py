temp = float(input('Insira uma temperatura em °C: '))
tipo = int(input('\nDeseja alterar para qual temperatura?\n\n1 - Graus F (Fahrenheit)\n2 - Graus K (Kelvin)\n3 - Graus RE (Réaumur)\n'))
while tipo not in [1, 2, 3]:
    tipo = int(input('\nEscreva um valor válido.\nDeseja alterar para qual temperatura?\n\n1 - Graus F (Fahrenheit)\n2 - Graus K (Kelvin)\n3 - Graus RE (Réaumur)\n'))
if tipo == 1:
    print(f'A temperatura em Fahrenheit é de: {temp * 1.8 + 32:.1f}')
elif tipo == 2:
    print(f'A temperatura em Kelvin é de: {temp + 273.15:.1f}')
else:
    print(f'A temperatura em Réuamur é de: {temp * 0.8:.1f}')