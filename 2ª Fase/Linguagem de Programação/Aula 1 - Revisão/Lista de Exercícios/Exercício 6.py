nome = input('Qual seu nome? ')
idade = int(input('Quantos anos você tem? '))
while idade > 130 or idade < 0:
    idade = int(input('\nInsira uma idade válida:\nQuantos anos você tem? '))
if idade < 16:
    print('Você é um não votante.')
elif idade <= 17 or idade > 65:
    print('Você é um eleitor facultativo.')
else:
    print('Você é um eleitor obrigatório.')