carros = {  1 : [ "fiat", "palio", "ano 2022", "prata"], 
            2 : [ "ford", "fiesta", "ano 2023", "branco"],
            3 : [ "honda", "fit", "ano 2024", "preto"]
        }
sair = False
print('Seja muito bem vindo a revenda de carros! ')
print('Carros já cadastrados:')
for v in carros:
    print(f"{v} --> {carros.get(v)}")
while sair == False:
    opcaoMenu = input("\nQual opção você deseja?\n\n1 - Cadastrar\n2 - Excluir\n3 - Pesquisar\n4 - Sair\n\nEscreva aqui o número da opção: ")
    while opcaoMenu not in ["1", "2", "3", "4"]:
        opcaoMenu = input("\nEscolha uma opção válida:\n\nQual opção você deseja?\n\n1 - Cadastrar\n2 - Excluir\n3 - Pesquisar\n4 - Sair\n\nEscreva aqui o número da opção: ")
    if opcaoMenu == "1":
        marca = input('Qual a marca do carro? ')
        modelo = input("Qual o modelo do carro? ")
        ano = int(input("Qual o ano do carro? "))
        anoFinal = f"ano {ano}"
        cor = input("Qual a cor do carro? ")
        print(f"Qual será o código do carro? Os códigos já utilizados são:\n")
        for v in carros.keys():
            print(v)
        codigo = int(input(f"\nEscolha um código diferente dos anteriores e que seja um número positivo: "))
        while codigo in carros.keys() or codigo < 0:
            codigo = int(input(f"\n\nPor favor, escolha um código diferente dos anteriores e que seja um número positivo: "))
        carros.update({codigo: [marca, modelo, anoFinal, cor]})
    elif opcaoMenu == "2":
        print(f"Qual carro você deseja excluir? Os carros já cadastrados são:\n")
        for v in carros:
            print(f"Código: {v} --> {carros.get(v)}")
        while True: 
            codigo = int(input("Escolha um dos códigos acima ou, se desejar cancelar a ação, escreva o número -1: "))
            if codigo != -1 and codigo not in carros.keys():
                print(f"\n\nPor favor, escolha um código pláusivel: ")
            elif codigo == -1:
                print('Ok.')
                break
            else:
                del carros[codigo]
                print("Veículo retirado da lista.")
                break
    elif opcaoMenu == "3":
        print('Qual o código do veículo que desejas saber as informações? Os códigos disponíveis são:')
        for v in carros.keys():
            print(v)
        codigo = int(input('Qual deseja? '))
        while codigo not in carros.keys():
            codigo = int(input(f"\n\nPor favor, escolha um código pláusivel: "))
        print(f'\n{codigo} --> {carros.get(codigo)}')
    elif opcaoMenu == "4":
        sair = True
        print("Ok! Obrigado por sua cooperação!")
