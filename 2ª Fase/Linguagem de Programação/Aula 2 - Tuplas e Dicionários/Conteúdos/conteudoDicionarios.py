# declarando dicionários
carrosVrummVrumm = {"marca": "Chevrolet", "modelo": "onix", "ano": 2021}
print(carrosVrummVrumm)

# acessando dados de um dicionário

    # acessando com colchetes (o código trava caso a chave não exista)
print(carrosVrummVrumm["marca"])
print(carrosVrummVrumm["modelo"])
print(carrosVrummVrumm["ano"])

    # acessando com a função get() (o código NÃO trava caso a chave não exista, somente aparecendo uma mensagem de erro)
print(carrosVrummVrumm.get("marca"))
print(carrosVrummVrumm.get("modelo"))
print(carrosVrummVrumm.get("ano"))

print(carrosVrummVrumm.get("placa", "chave não encontrada")) # irá aparecer o texto de depois da vírgula caso a chave não exista



# acessando as chaves do dicionário
print(carrosVrummVrumm.keys())

# acessando os valores do dicionário
print(carrosVrummVrumm.values())

# acessando as chaves e os valores
print(carrosVrummVrumm.items())

# atribuindo e alterando valores
carrosVrummVrumm["placa"] = "AQM1T64"
carrosVrummVrumm["placa"] = "MOP9I12"
print(carrosVrummVrumm.get("placa"))

carrosVrummVrumm.update({"cor": "preto"}) # é literalmente igual ao de cima
print(carrosVrummVrumm.get("cor"))



# deletando valores do dicionário

    # com pop
a = carrosVrummVrumm.pop("cor")

    # com del
del carrosVrummVrumm["placa"]

print(carrosVrummVrumm.items())

# verificando de o item existe no dicionário
print("marca" in carrosVrummVrumm) # True
print("placa" in carrosVrummVrumm) # False



# utilizando for

    # retornando chaves
for v in carrosVrummVrumm:
    print(v)

    # retornando valores
for v in carrosVrummVrumm.values():
    print(v)

    # retornando chaves e valores
for chave, valor in carrosVrummVrumm.items():
    print(f"{chave}: {valor}")

filmesLista = [{"Nome": "Filmes"}]

for v in range(3):
    filmes = {}
    nome = input("Nome do filme: ")
    genero = input("Digite o gênero: ")
    filmes.update({"Nome": nome})
    filmes.update({"Gênero": genero})
    filmesLista.append(filmes)
    print(filmesLista)
for v in range (3):
    print(f'{filmesLista[v]["Nome"]} --> {filmesLista[v]["Gênero"]}')
    
