tuplaValores, numPares = (), []
for v in range(4):
    valor = int(input("Digite um valor aleatório: "))
    tuplaValores += (valor,)
    if valor % 2 == 0:
        numPares.append(valor)
print(f"a) O 9 foi digitado {tuplaValores.count(9)} vezes")
print(f"b) O 3 foi digitado pela primeira vez no {tuplaValores.index(3) + 1}")
print(f"c) Os números pares foram: {numPares}")