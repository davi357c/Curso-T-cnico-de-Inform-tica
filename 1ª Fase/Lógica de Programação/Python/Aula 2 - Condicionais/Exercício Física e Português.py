while True:
    disciplina = input(f'Qual a sua disciplina, fisica ou portugues?').lower()
    if disciplina=="fisica":
        while True:
            nTeorica = float(input(f'Qual sua nota de física teórica?'))
            nPratica = float(input(f'Qual sua nota de física prática?'))
            if nTeorica>4 or nPratica>6 or nTeorica or nPratica<0:
                print(f'Notas inválidas')
            else:
                break
        nFinal = nTeorica+nPratica
        print(f'Sua nota total foi de {nFinal}!')
        break
    elif disciplina=="portugues":
        while True:
            nTeorica = float(input(f'Qual sua nota de português teórica?'))
            nPratica = float(input(f'Qual sua nota de português prática?'))
            if nTeorica or nPratica>5 or nTeorica or nPratica<0:
                print(f'Notas inválidas')
            else:
                break
        nFinal = nTeorica+nPratica
        print(f'Sua nota total foi de {nFinal}!') 
        break
    else:
        print(f'Disciplina inválida')