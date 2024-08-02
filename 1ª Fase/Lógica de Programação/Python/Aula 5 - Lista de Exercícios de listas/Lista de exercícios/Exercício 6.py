counter, nota_final = 0, 0
for v in range(10):
    counter2 = 0
    counter+=1
    name = input(f'Qual a nota do {counter}º aluno? ')
    for v in range(4):
        counter2+=1
        nota = float(input(f'Qual a {counter2}º nota do aluno? '))
        nota_final += nota
    media = nota_final/4