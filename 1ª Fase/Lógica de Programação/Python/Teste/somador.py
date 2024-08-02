numbers = []
x = float(input(f'Digite um número'))
numbers.append(x)
while x != 0:
    x = float(input(f'Digite um número'))
    numbers.append(x)
print(sum(numbers))