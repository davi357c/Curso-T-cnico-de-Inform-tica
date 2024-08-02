c1, c2, c3, counter= 0, 0, 0, 0
votantes = int(input('Quantas pessoas irão votar? '))
for v in range(votantes):
    counter+=1
    votos = int(input(f'Votante {counter}, você deseja votar em qual candidato?\n1 - Candidato 1\n2 - Candidato 2\n3 - Candidato 3\n'))
    while votos not in [1, 2, 3]:
        votos = int(input('Escolha uma opção válida.\nVocê deseja votar em qual candidato?\n1 - Candidato 1\n2 - Candidato 2\n3 - Candidato 3\n'))
    if votos == 1:
        c1+=1
    elif votos == 2:
        c2+=1
    elif votos == 3:
        c3+=1
    print(f'\n\n\n\n')
print(f'Candidato 1 ---> {c1} votos\nCandidato 2 ---> {c2} votos\nCandidato 3 ---> {c3} votos')