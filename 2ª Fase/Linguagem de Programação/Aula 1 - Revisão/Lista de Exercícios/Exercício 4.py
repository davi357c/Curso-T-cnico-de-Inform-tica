nome = input('Qual o nome do paciente? ')
idade = int(input('Qual a idade do paciente? '))
while idade > 130 or idade < 0:
    idade = int(input('\nInsira uma idade válida:\nQual a idade do paciente? '))
peso = float(input('Qual o peso do paciente? '))
if idade <= 15:
    print('Pessoas de 0 a 15 anos não podem ser doadores por estarem abaixo da idade permitida')
elif idade <= 17:
    print('Pessoas de 16 e 17 anos e que estejam pesando mais de 55 kg, podem ser doadores com autorização dos pais ou responsáveis.')
    if peso < 55:
        print(f'Você não pode doar pois pesa menos que o permitido!')
elif idade <= 69:
    print('Pessoas de 18 a 69 e que estejam pesando mais de 60 kg, podem ser doadores.')
    if peso < 60:
        print(f'Você não pode doar pois pesa menos que o permitido!')
else:
    print('Pessoas acima de 69 anos não podem ser doadores por estarem acima da idade permitida.')