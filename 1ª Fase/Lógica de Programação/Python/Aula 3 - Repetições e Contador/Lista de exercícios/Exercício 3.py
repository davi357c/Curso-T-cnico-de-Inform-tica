b = c = int(input(f'Escoha um número: ')) 
for v in range(9):
    a = int(input(f'Escoha um número: '))
    if a>b:
        b=a
    if a<c:
        c=a
print(f'O maior número digitado foi: {b}\nO menor número digitado foi: {c}')
