name = input(f'Qual o seu nome?')
while len(name)<3:
    name = input(f'Escreva um nome acima de 3 letras:\nQual o seu nome?')
age = int(input(f'Qual a sua idade?'))
while age>100 or age<0:
    age = int(input(f'Idade inválida:\nQual a sua idade?')) 
salary = float(input(f'Qual seu salário?'))
while salary<=0:
    salary = float(input(f'Salario inválido\nQual seu salário?'))
gender = input(f'Qual seu gênero? (M ou F)').lower()
while gender not in ('m', 'f'):
    gender = input(f'Digite um genero válido\nQual seu gênero? (M ou F)').lower()
maritalstatus = input(f'Qual seu estado civil? (S, C, V ou D)').lower()
while maritalstatus not in ('s', 'c', 'v', 'd'):
    maritalstatus = input(f'Digite um estado civil válido\nQual seu estado civil? (S, C, V ou D)').lower()
print(f'Tudo correto!')