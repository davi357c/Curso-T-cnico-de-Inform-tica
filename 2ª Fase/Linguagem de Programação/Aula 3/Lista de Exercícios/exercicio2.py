top20CampeonatoBrasil = "Botafogo", "Fortaleza", "Flamengo", "Palmeiras", "São Paulo", "Cruzeiro", "Bahia", "Athletico-PR","Atlético-MG", "Vasco da Gama", "Bragantino", "Juventude", "Grêmio", "Criciúma", "Internacional", "EC Vitória", "Corinthians", "Fluminense", "Cuiabá", "Atlético-GO"
print(f'a) Os 5 primeiros colocados são: {top20CampeonatoBrasil[:5]}')
print(f'b) Os 5 últimos colocados são: {top20CampeonatoBrasil[-4:]}')
print(f'c) Os time em ordem alfabética são: {sorted(top20CampeonatoBrasil)}')
print(f'd) O Criciúma está na posição: {top20CampeonatoBrasil.index("Criciúma")}')
