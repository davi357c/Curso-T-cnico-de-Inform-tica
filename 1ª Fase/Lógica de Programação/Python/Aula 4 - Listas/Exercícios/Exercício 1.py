list_names, list_grades, final_grades = [], [], {}
studants = input(f'De quais studants você gostaria de registrar as notas?\nDigite "Parar" se deseja parar com a lista.\n').title()
while studants != "PARAR":
    list_names.append(studants)
    studants = input().title()
for names in list_names:
    grades = float(input(f'Média do aluno "{names}": '))
    final_grades[names] = grades
final_grades

""" studant_and_grade, list_names, counter = [], [], 1
studants = input(f'De quais studants você gostaria de registrar as notas?\nDigite "Parar" se deseja parar com a lista.\n').title()
while studants != "Parar":
    list_names.append(studants)
    studants = input().title()
for names in list_names:
    grades = float(input(f'Média do aluno "{names}": '))
    studant_and_grade.append(f'{grades} -> {names}')
studant_and_grade.sort(), studant_and_grade.reverse()
for final_grades in studant_and_grade:
    print(f'{counter}- {final_grades}')
    counter+=1 

print(type(studant_and_grade))"""