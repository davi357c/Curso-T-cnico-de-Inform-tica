list_items = []
for v in range(5):
    item = input('Escreva um item: ')
    list_items.append(item)
new_list_items = list_items   #Para a lista original ficar inteira
for items in new_list_items:
    if new_list_items.count(items) > 1:
        print(f'{items} -> {new_list_items.count(items)}')
        for v in range(new_list_items.count(items)):
            new_list_items.remove(items)
