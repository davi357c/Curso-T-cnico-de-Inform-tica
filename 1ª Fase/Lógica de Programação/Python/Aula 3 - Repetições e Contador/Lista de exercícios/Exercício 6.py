a = 'sim'
cont = 1
num = int(input(f'Escolha um número: '))
while num>cont+1 and a=='sim':
    cont+=1
    b=num%cont
    if b==0:
        a='não'
if a=='não' or num==1:
    print(f'Esse não é um número primo')
else:
    print(f'Esse número é primo')