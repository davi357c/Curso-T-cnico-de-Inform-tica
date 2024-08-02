tasks = ['estudar', 'fazer comida', 'caminhar', 'jogar', 'dormir', 'ler', 'arrumar a casa', 'tomar café']
test = [1, 2, 3, 4, 'fazer lição de casa', True]

""" #Fazer por index
print(tasks[0])
print(tasks[1])
print(tasks[2])

print(tasks[-1])
print(tasks[-2])
print(tasks[-3])

#Acessar inervalos da lista
print(tasks[1:4])
print(tasks[0:3])

print(tasks[:3])
print(tasks[3:]) """

#Adicionar itens na lista pelo index

#append() adiciona sempre ao final da lista
tasks2 = []
tasks2.append('estudar física')
tasks2.append('fazer dever de casa')
tasks2.append('fazer café da manhã')
tasks2.append('lavar a louça')

#insert() adiciona o item na posição desejada
tasks2.insert(0, 'ler')
print(tasks2[0:])

#Altera o valor do item na posição desejada
tasks2[0] = 'limpar a casa'

#Deletar itens de uma lista

#remove() retira um item específico da lista pelo seu valor
tasks2.remove('estudar física')
print(tasks2)

#del utiliza o index do item para excluir
del tasks2[1]
print(tasks2)

#pop() deleta o último item da lista ou pelo index

#Sem parâmetros
tasks2.pop()
print(tasks2)

#Com parâmetros
tasks2.pop(1)
print(tasks2)

#Salvando em outra variável
tarefa   = tasks2.pop(0)
print(f'{tarefa}, {tasks2}')

#sort() ordena a lista (não dá pra misturar types)
values = [1, 4, -15, 214, 123, 123, 8]
values.sort()
print(values)

#reverse() inverte a ordem da lista
values.reverse()
print(values)

#len() retorna a quantia de valores dentro da lista
print(len(values))

#Retornar maiores e menores valores, seja float ou string (Iniciais, ou seja, em ordem alfabética)

#max() retorna o maior valor
value_max = max(values)
print(f'Maior valor: {value_max}')

#min() retorna o menor valor
value_min = min(values)
print(f'Menor valor: {value_min}')

#copy() cria uma nova lista a partir das informações de outra lista
values_new = values.copy()
print(f'values_new: {values_new}')

#clear() limpa a lista, sem que ela seja excluida
values.clear()
print(f'values: {values}')

#sum() soma os valores de uma lista
soma_lista = sum(values_new)
print(soma_lista)

#count() retorna quantos de um valor específico tem na lista
print(values_new.count(123))

#index() retorna a posição do item na lista
print(values_new.index(-15))

#Concateanar (juntar duas listas)
new_list = values_new + tasks
print(new_list)