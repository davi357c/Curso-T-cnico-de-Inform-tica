from math import pi
def areaCirculo():
    raio = float(input("\nQual a raio do círculo? "))
    area = pi*raio**2
    return area
def areaRetangulo(base, altura):
    area = base * altura
    return area
def areaTriangulo(base, altura):
    area = base * altura / 2
    return area
sair = False
while sair != True:
    menu = input("\nQual opção você deseja?\n\n1- Área de um retângulo\n2- Área de um triângulo\n3- Área de um círculo\n4- Sair\n\nEscreva o respectivo número da opção: ")
    while menu not in ["1", "2", "3", "4"]:
        menu = input("\n\nEscolha uma opção válida\n\nQual opção você deseja?\n\n1- Área de um retângulo\n2- Área de um triângulo\n3- Área de um círculo\n4- Sair\n\nEscreva o respectivo número da opção: ")
    if menu == "1" or menu == "2":
        base = float(input("\nQual a base? "))
        altura = float(input("Qual a altura? "))
        if menu == "1":
            print(f"\nA área do retângulo é de {areaRetangulo(base, altura)}")
        else:
            print(f"\nA área do triângulo é de {areaTriangulo(base, altura)}")
    elif menu == "3":
        print(areaCirculo())
    else:
        sair = True