nome = input('Qual seu nome? ')
peso = float(input('Qual seu peso? '))
altura = float(input('Qual seu altura? '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc <= 25:
    print('Você está com peso normal')
elif imc <=30:
    print('Você está acima do peso')
else:
    print('Você está obeso')