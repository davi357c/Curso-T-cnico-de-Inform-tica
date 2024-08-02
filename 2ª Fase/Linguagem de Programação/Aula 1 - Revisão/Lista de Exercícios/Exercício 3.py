nome = input('Qual o nome do aluno? ')
idade = int(input('Qual a idade do aluno? '))
while idade > 18 or idade < 0:
    idade = int(input('\nInsira uma idade válida:\nQual a idade do aluno? '))
if idade <= 2:
    estado = 'Berçário'
elif idade <= 6:
    estado = 'Educação Infantil'
elif idade <= 10:
    estado = 'Ensino Fundamental I'
elif idade <= 15:
    estado = 'Ensino Fundamental II'
else:
    estado = 'Ensino Médio'
print(f'O nível escolar do aluno é: {estado}')