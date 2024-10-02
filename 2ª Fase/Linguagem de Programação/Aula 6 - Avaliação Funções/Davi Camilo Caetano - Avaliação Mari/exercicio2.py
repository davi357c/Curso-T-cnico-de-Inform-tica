# Davi Camilo Caetano | 2137 | 18/09/2024

from functools import reduce    # Importa a função reduce da biblioteca functools

dicionarioFuncionariosSalarios = {}

sair = False
print("Por favor, não repita nomes e caso erre o salário de um funcionário digite o mesmo nome e o salário correto")
while sair not in ["s", "sim"]: # Lê quantos funcionários e salários o usuário quiser e adiciona eles num dicionário
    funcionario = input("\nQual o nome do funcionário? ").capitalize()
    salario = float(input(f"Qual o salário de {funcionario}? "))
    dicionarioFuncionariosSalarios.update({funcionario: salario})
    sair = input("Você deseja parar por aqui? (S ou N) ").lower().strip()

salarioMinimo = float(input("\nQual o salário mínimo? (Sua escolha) "))
funcionariosFiltrados = dict(filter(lambda x: x[1] > salarioMinimo, dicionarioFuncionariosSalarios.items())) # Filtra os funcionários que tem o salário acima do definido
print(f"\nb) Os funcionários de salário acima do mínimo são: {funcionariosFiltrados}")

salariosAtualizados = dict(map(lambda x: (x[0], x[1] * 1.20), funcionariosFiltrados.items()))   # Aumenta em 20% o salário dos funcionários filtrados
print(f"\nc) Aumento de 20% para os funcionarios acima do mínimo: {salariosAtualizados}")

dicionarioFuncionariosSalarios.update(salariosAtualizados)  # Atualiza os 20% aumentados no dicionário com todos os funcionários
print(dicionarioFuncionariosSalarios)
print(f"d) A média salárial de todos os funcinários da empresa é: {sum(dicionarioFuncionariosSalarios.values())/len(dicionarioFuncionariosSalarios)}")

print(f"e) O funcionário com mais salário é {reduce(lambda x, y: x if x[1] > y[1] else y, dicionarioFuncionariosSalarios.items())} e o com menos salário é {reduce(lambda x, y: x if x[1] < y[1] else y, dicionarioFuncionariosSalarios.items())}") # Utiliza a função reduce para mostrar somente o maio e menor salário