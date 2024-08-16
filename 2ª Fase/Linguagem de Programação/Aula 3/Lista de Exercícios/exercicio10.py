todasAgendas = []
for v in range(5):
    agenda = {}
    agenda.update({"cpf": input("Digite seu cpf: ")})
    agenda.update({"nome": input("Digite seu nome: ")})
    agenda.update({"idade": input("Digite sua idade: ")})
    agenda.update({"telefone": input("Digite seu telefone: ")})
    todasAgendas.append(agenda)
for v in todasAgendas:
    print()