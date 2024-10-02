# Davi Camilo Caetano | 2137 | 18/09/2024

meses = "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
listaReceitas, listaDespesas = [], []   # Definindo os meses e as listas

for v in meses: # Vai ler até a lista meses acabar ou o usuário sair
    receita = float(input(f"\nQual a receita do mês de {v}? "))
    listaReceitas.append(receita)
    despesa = float(input(f"Quais as despesas do mês de {v}? "))
    listaDespesas.append(despesa)
    sair = input("Você deseja parar por aqui? (S ou N) ").lower().strip()
    if sair in ["s", "sim"]:
        break

listaLucroMensal = list(map(lambda x, y: x - y, listaReceitas, listaDespesas))  # Vai fazer a subtração das receitas e despesas

print(f"\na) O lucro líquido de casa mês é {listaLucroMensal}") # Vai mostrar o lucro líquido mensal

if len(listaReceitas) < 12: # Verifica se o usuário colocou todos os meses, para uma gama mais variada de respostas
    print(f"\nb) O lucro médio anual é {sum(listaLucroMensal) / len(listaLucroMensal)} caso os meses faltantes continuem com a mesma média")
else:
    print(f"\nb) O lucro médio anual é {sum(listaLucroMensal) / len(listaLucroMensal)}")

dicionarioAuxiliar, counter = {}, 0
for x in listaLucroMensal:  
    dicionarioAuxiliar.update({meses[counter]: x}) # Faz um dicionários com os meses e os lucros de cada mes
    counter += 1
print(f"\nc) Os meses que tiveram prejuízo foram: {dict(filter(lambda x: x[1] < 0, dicionarioAuxiliar.items()))}") # Exibe somente os meses que o lucro for negativo