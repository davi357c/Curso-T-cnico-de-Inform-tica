n=1
while n!=0:
    n = int(input('Escreva um número inteiro: '))
    r = n%2
    if r==1:
        print(f'O número digitado é impar')
    else:
        print(f'O número digitado é par')

