lista = []
n = input("Digite um nome: ").title()
while n != "-12345":
    lista.append(n)
    n = input("Digite outro nome, caso queira parar, digite -12345: ").title()
print(f'Os nomes que começam com "A" {list(filter(lambda x: x.startswith("A"), lista))}')