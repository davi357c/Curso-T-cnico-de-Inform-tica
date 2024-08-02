list = []
number = float(input('Escolha um número: '))
list.append(number)
while number != 0:
    number = float(input('Escolha um número: '))
    list.append(number)
print(f'Maior: {max(list)}\nMenor: {min(list)}')