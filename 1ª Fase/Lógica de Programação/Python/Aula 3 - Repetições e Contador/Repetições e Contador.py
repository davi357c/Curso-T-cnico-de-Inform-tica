i = 0
while i<10:
    i+=1   #Contador
    print(i)
print(f'Acabou!')

#Exemplo for lista
for i2 in [14,2246,4457,51345,26678]:
    print(f'{i2}*4 = {i2*4}')

#Exemplo for range
    #start, stop
    for i2 in range (-15,10):
        print(f'{i2}*4 = {i2*4}')
    #start, stop, step
    for i2 in range (-15,10,3):
        print(f'{i2}*4 = {i2*4}')
    #stop
    for i2 in range (10):
        print(f'{i2}*4 = {i2*4}')

print(list(range(10,16)))
print(list(range(16,10,-1)))

#for percorre por cada letra da palavra
palavra = "cachorro"
for i3 in palavra:
    print(i3)

#for por lista mas com variável para lista
mercado = ['café', 'pão', 'chocolate']
for i4 in mercado:
    print (i4)