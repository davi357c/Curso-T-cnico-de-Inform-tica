while True:    
    n1 = float(input(f'Qual sua primemira nota? (Peso 5) '))
    if n1<0 or n1>5:
        print(f'Escreva a nota correta')
    else:
        break
while True:    
    n2 = float(input(f'Qual sua segunda nota? (Peso 5) '))
    if n2<0 or n2>5:
        print(f'Escreva a nota correta')
    else:
        break
while True:    
    n3 = float(input(f'Qual sua terceira nota? (Peso 10) '))
    if n3<0 or n3>10:
        print(f'Escreva a nota correta')
    else:
        break
media=(n1+n2+n3)/2
print(f'Sua média é de: {media}')
if media<6:
    print(f'Você foi reprovado')
else:
    print(f'Você foi aprovado!')