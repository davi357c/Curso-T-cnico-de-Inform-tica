# Davi Camilo Caetano | 2137 | 18/09/2024

dicionarioPedidos = {}

sair = False
while sair == False:    # Fica repitindo até sair ser diferente de false
    menu = input("\nQual opção deseja?\n\n1 - Adicionar Pedido\n2 - Atualizar Pedido\n3 - Remover Pedido\n4 - Filtrar Pedidos\n5 - Visualizar Todos os Pedidos\n6- Sair\n\nEscreva o repectivo número aqui --> ")
    while menu not in ["1", "2", "3", "4", "5", "6"]:   # Repetição caso não escolha opção válida
        menu = input("\nEscolha uma opção válida: ")

    if menu == "1":
        nome = input("Qual o nome do cliente? ").capitalize()
        listaPratos = []
        parar = False
        while parar not in ["s", "sim"]:    # Repetição até o usuário escolher parar
            prato = input(f"Qual prato o cliente pediu? ").capitalize()
            listaPratos.append(prato)   # Adiciona a variável prato na lista listaPratos
            parar = input("Você deseja parar por aqui? (S ou N) ").lower().strip()
        dicionarioPedidos.update({nome: listaPratos})   # Adiciona o pedido no dicionário

    elif menu == "2":
        nome = input(f"De qual cliente deseja alterar o pedido? As opções são {list(dicionarioPedidos.keys())}. ").capitalize()
        while nome not in dicionarioPedidos.keys(): # Verifica se o nome está nas keys do dicionário
            nome = input("\nEscolha uma opção válida: ").capitalize()
        pedidoAntigo = dicionarioPedidos.get(nome)  # Pega o value da key nome
        prato = input(f"Qual prato você deseja alterar? As opções são {pedidoAntigo}").capitalize() # mostra as opções de pedidos
        while prato not in pedidoAntigo:
            prato = input("\nEscolha uma opção válida: ").capitalize()
        novoPrato = input("Qual prato será colocado no lugar? ").capitalize()
        pedidoAntigo[pedidoAntigo.index(prato)] = novoPrato # Substitui o prato na lista
        dicionarioPedidos.update({nome: pedidoAntigo}) # Atualiza no dicionário
        print("Prato alterado")

    elif menu == "3":
        nome = input(f"De qual cliente deseja excluir um prato? As opções são {list(dicionarioPedidos.keys())}. ").capitalize()
        while nome not in dicionarioPedidos.keys(): # Verifica se o nome está nas keys do dicionário
            nome = input("\nEscolha uma opção válida: ").capitalize()
        pedidoAntigo = dicionarioPedidos.get(nome)  # Pega o value da key nome
        prato = input(f"Qual prato você deseja excluir? As opções são {pedidoAntigo}").capitalize()
        while prato not in pedidoAntigo:
            prato = input("\nEscolha uma opção válida: ").capitalize()
        pedidoAntigo.pop(pedidoAntigo.index(prato)) # Retira o pedido especifico do cliente
        print("Prato removido")

        if dicionarioPedidos.get(nome) == []: # Verifica se o cliente ainda tem pratos e caso não tenha exclui o pedido
            dicionarioPedidos.pop(nome)

    elif menu == "4":
        nome = input(f"De qual cliente deseja filtrar o pedido? As opções são {list(dicionarioPedidos.keys())}. ").capitalize()
        while nome not in dicionarioPedidos.keys(): # Verifica se o nome está nas keys do dicionário
            nome = input("\nEscolha uma opção válida: ").capitalize()
        print(f"\nOs pratos cadastrados por este cliente são: {dicionarioPedidos.get(nome)}")   # Pega o value da key nome

    elif menu == "5":
        for x, y in dicionarioPedidos.items(): # Mostra os pedidos de todos os clientes
            print(f"{x} --> {y}")
    
    elif menu == "6":
        sair = True # Sai do programa
print("Programa finalizado.")