produtos= "Maçã", 1.99, "Banana", 2.99, "Cenoura", 2.49, "Melância", 8.29, "Goiaba", 4.89
counterProdutos, counterPrecos = 0, 1
for v in range(len(produtos)//2):
    print(f"{produtos[counterProdutos]} --> R$ {produtos[counterPrecos]}")
    counterProdutos += 2
    counterPrecos += 2
