list, count, count2 = [], 1, 1
item = input(f'Digite "Parar" se deseja parar com a lista.\nProduto {count}: ').capitalize()
while item != 'Parar':
    count+=1
    list.append(item)
    item = input(f'Produto {count}: ').capitalize()
for v in list:
    print(f'{count2}- {v}')
    count2+=1