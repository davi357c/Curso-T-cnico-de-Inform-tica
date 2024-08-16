mediaDict = {}
nome = input("Qual o nome do aluno? ")
mediaDict.update({"nome": nome})
media = float(input("Qual a media do aluno? "))
mediaDict.update({"media": media})
if mediaDict.get("media") >= 7:
    print("Aprovado")
else:
    print("Reprovado")
