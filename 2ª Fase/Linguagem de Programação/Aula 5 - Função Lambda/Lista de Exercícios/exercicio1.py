lista = []
n = int(input("Digite um número: "))
while n != -12345:
    n = int(input("Digite outro número, caso queira parar, digite -12345: "))
    lista.append(n)
print(f"Os números pares são: {list(filter(lambda x: x%2==0, lista))}")
