tipo = input('Qual o tipo do combustível? Álcool (A) ou gasolina (G)? ').lower()
quantia = float(input('Quantos litros foram colocados? '))
if tipo == 'a':
    preco = quantia * 4.22
    if quantia <= 20:
        precoFinal = preco - (preco * 0.03) * quantia
    elif quantia > 20:
        precoFinal = preco - (preco * 0.05) * quantia
if tipo == 'g':
    preco = quantia * 5.65
    if quantia <= 20:
        precoFinal = preco - (preco * 0.04) * quantia
    elif quantia > 20:
        precoFinal = preco - (preco * 0.06) * quantia
print(f'O ppreço final é de: {precoFinal}')