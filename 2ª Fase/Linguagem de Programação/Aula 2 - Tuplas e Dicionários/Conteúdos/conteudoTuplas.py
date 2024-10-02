# declara a tupla
minhaTupla = (1, 2, "programação", True, 1.6)
print(type(minhaTupla))

minhaTupla2 = 1, 2, "programação", True, 1.6
print(type(minhaTupla))



# acessando os valores de uma tupla

    #  acessar um item pelo index
print(minhaTupla[4])

print(minhaTupla[-2])

    # acessando por intervalos
print(minhaTupla[:2]) # pega somente os dois primeiros itens
print(minhaTupla[:-2]) # pega até o anterior do penultimo item

print(minhaTupla[2:]) # vai começar do terceiro valor
print(minhaTupla[-2:]) # vai começar do penultimo valor



# concatenando tuplas
tuplaConcatenada = minhaTupla + minhaTupla2
print(tuplaConcatenada)

tuplaReplicada = minhaTupla * 3
print(tuplaReplicada)



# min e max
# valorMinimo = min(minhaTupla) <--- (os dois não vão dar certo, visto que tem diferentes types de variáveis dentro da tupla)
# valorMaximo = max(minhaTupla) <---

tuplaNumeros = 1, 2, 99, 4, -2
valorMinimo = min(tuplaNumeros)
valorMaximo = max(tuplaNumeros)  



# não tem .sort(), mas tem .sorted(), que não altera diretamente a variável



# retirar variáveis das tuplas

tuplaNova = 1, 2, 3
x, y, z = tuplaNova

print(f'{x}, {y} e {z}')



# função enumerate()

frutas = ("maçã", "ameixa", "banana", "melancia", "uva")

for indice, v in enumerate(frutas, 1): # o indice pega do enumerate e o v pega do frutas
    print(f'{indice}- {v}')

