lista = []
n = input("Digite um palavra: ").lower()
while n != "-12345":
    lista.append(n)
    n = input("Digite outro palavra, caso queira parar, digite -12345: ").lower()
print(list(map(lambda x: f"{len(x)} --> {x}", list(filter(lambda x: len(x) > 3, lista)))))