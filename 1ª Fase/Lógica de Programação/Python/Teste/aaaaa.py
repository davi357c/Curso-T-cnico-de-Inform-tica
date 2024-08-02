""" counter = -1
for v in cidades_vitimas:
    counter+=1
    if acidentes.index(counter)"""  

acidentes = []
min_acidente = min(acidentes)
quantia_cidades_min = acidentes.count(min_acidente)
for v in range(quantia_cidades_min):
    index = acidentes.index(min_acidente)
    acidentes.pop(index)