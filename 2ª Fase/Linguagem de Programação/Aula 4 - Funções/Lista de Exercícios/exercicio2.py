from math import sqrt
def soma(n1, n2):
    resultado = n1 + n2
    return resultado
def subtracao(n1, n2):
    resultado = n1 - n2
    return resultado
def multiplicacao(n1, n2):
    resultado = n1 * n2
    return resultado
def divisao(n1, n2):
    resultado = n1 / n2
    return resultado
def potenciacao(n1, n2):
    resultado = n1 ** n2
    return resultado
def raiz(n):
    resultado = sqrt(n)
    return resultado
sair = False
while sair != True:
    menu = input("\nQual opção você deseja?\n\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Potenciação\n6- Raiz quadrada\n7- Sair\n\nEscreva o respectivo número da opção: ")
    while menu not in ["1", "2", "3", "4", "5", "6", "7"]:
        menu = input("\n\nEscolha uma opção válida\n\nQual opção você deseja?\n\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Potenciação\n6- Raiz quadrada\n7- Sair\n\nEscreva o respectivo número da opção: ")
    if menu in ["1", "2", "3", "4", "5"]:
        n1 = float(input("Qual o primeiro número?"))
        n2 = float(input("Qual o segundo número?"))
        if menu == "1":
            print(f"O resultado é: {soma(n1, n2)}")
        elif menu == "2":
            print(f"O resultado é: {subtracao(n1, n2)}")
        elif menu == "3":
            print(f"O resultado é: {multiplicacao(n1, n2)}")
        elif menu == "4":
            print(f"O resultado é: {divisao(n1, n2)}")
        elif menu == "5":
            print(f"O resultado é: {potenciacao(n1, n2)}")
    elif menu == "6":
        n = float(input("Qual o número?"))
        print(f"O resultado é: {raiz(n)}")
    else: 
        sair = True