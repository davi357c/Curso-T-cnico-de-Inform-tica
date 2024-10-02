lista = []
n = int(input("Digite um número: "))
while n != -12345:
    lista.append(n)
    n = int(input("Digite outro número, caso queira parar, digite -12345: "))
print(list(map(lambda x: x**2, lista)))