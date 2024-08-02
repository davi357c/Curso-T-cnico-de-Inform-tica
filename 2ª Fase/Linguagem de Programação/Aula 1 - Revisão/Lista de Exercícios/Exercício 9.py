alturaMulheres, alturaHomens = [], []
for v in range(50):
    sexo = input('Qual seu sexo? Masculino (M) ou Feminino (F)? ').lower()
    while sexo not in ['m', 'f']:
        sexo = input('Escolha uma opção válida.\nQual seu sexo? Masculino (M) ou Feminino (F)? ').lower()
    altura = float(input('Qual a sua altura? '))
    if sexo == 'm':
        alturaHomens.append(altura)
    else:
        alturaMulheres.append(altura)
alturaTodeskk = alturaHomens + alturaMulheres
print(f'a) A maior altura do grupo é: {max(alturaTodeskk)}\n   A menor altura do grupo é: {min(alturaTodeskk)}')
print(f'b) A média de altura das mulheres é: {sum(alturaMulheres)/len(alturaMulheres)}')
print(f'c) O número de homens é de: {len(alturaHomens)}')
print(f'd) A porcentagem de homens é de: {len(alturaHomens*2)}%\n   A porcentagem de mulheres é de: {len(alturaMulheres*2)}%')