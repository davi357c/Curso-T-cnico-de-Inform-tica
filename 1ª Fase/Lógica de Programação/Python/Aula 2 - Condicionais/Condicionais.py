""" n1 = float(input(f'Quanto tiraste em tua primeira nota?'))
n2 = float(input(f'Quanto tiraste em tua segunda nota?'))
media=(n1+n2)/2
print(f'Tua média é: {media}')
if media>=5 and media<7:
    print(f'Estás em recuperação!')
elif media>=0 234and media<5:
    print(f'Foste reprovado!')
elif media>=7 and media<=10:
    print(f'Passaste!!!')
else:
    print(f'Tuas notas estão invalidas!!!!!!!') """

while True:
    n1 = float(input(f'Quanto tiraste em tua primeira nota?'))
    if n1>10 or n1<0:
        print(f'Notas inválidas')     
    else:
        break
while True:
    n2 = float(input(f'Quanto tiraste em tua segunda nota?'))
    if n2>10 or n2<0:
        print(f'Notas inválidas')
    else:
        break
media=(n1+n2)/2
print(f'Tua média é: {media}')
if media>=5 and media<7:
    print(f'Estás em recuperação!')
elif media>=0 and media<5:
    print(f'Foste reprovado!')
elif media>=7 and media<=10:
    print(f'Passaste!!!')
else:
    print(f'Tuas notas estão invalidas!!!!!!!')