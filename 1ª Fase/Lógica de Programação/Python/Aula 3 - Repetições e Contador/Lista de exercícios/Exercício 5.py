num = a = b = c = 0
d = float('inf')
e = float('-inf')
while not num==-1:
    num = int(input(f'Digite um número: '))
    if num>0:
        c+=1
        a+=num
        if d>num:
            d=num
        if e<num:
            e=num
    elif num<0 and num>-1 or num<-1:
        print(f'Somente números positivos são permitidos')
b=a/c
print(f'A soma dos valores é: {a}\nA média dos valores é: {b}\nO maior número é: {e}\nO menor número é: {d}')
