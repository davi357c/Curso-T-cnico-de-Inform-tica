lista = []
n = input("Digite um nome: ").title()
while n != "-12345":
    lista.append(n)
    n = input("Digite outro nome, caso queira parar, digite -12345: ").title()
print(sorted(lista, key=lambda x: len(x)))