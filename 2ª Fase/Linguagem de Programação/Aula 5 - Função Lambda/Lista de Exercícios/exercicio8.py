from functools import reduce

lista = []
n = int(input("Digite um número: "))
while n != -12345:
    lista.append(n)
    n = int(input("Digite outro número, caso queira parar, digite -12345: "))
print(reduce(lambda x, y: x * y, lista))