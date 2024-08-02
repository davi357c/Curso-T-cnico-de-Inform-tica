nome = 'Davi'                                                                                                                          #Variveis
idade = 15
custobeneficio = 13.99
custoporidade = custobeneficio/idade


print ('Hello world!')                                                                                      #print normal (Pra escrever na tela)
print (type (nome))
print (type (idade))
print (type (custobeneficio))

print(f'O valor do custo benefício por idade é de:{custobeneficio/idade:.2f}')                                                      #print formatado

Grrr = float (input ('How many Grrrrrrsss did you give yesterday?'))                      #input normal (Pra perguntar e responder e com class) 
print ('WOW!', Grrr,"Grrrrrrsss!? That's a lot of Grrrrrrrsss!!!")

Grrr = float (input (f'{nome}, how many Grrrrrrsss did you give yesterday?'))                                                   #input formatado
print (f"WOW! {Grrr} Grrrrrrsss!? That's a lot of Grrrrrrrsss!!!")

v1=10                   #Resultados de calculos diversos
v2=10
adicao=v1+v2
subtracao=v1-v2
multiplicacao=v1*v2
divisao=v1/v2
potenciacao=v1**2
raiz=v1**1/2
restodivisao=v1//3      #=1

print(v1.islower())
print(v1.isnumeric())

n=input('quaL seu nome?').upper()           #Faz com que tudo fique maiúsculo

n=input('quaL seu nome?').lower()           #Faz com que tudo fique minúsculo

n=input('quaL seu nome?').title()           #Faz com que cada palavra tenha sua inicial maiúscula

n=input('quaL seu nome?').capitalize()      #Faz com que a frase tenha sua inicial maiúscula