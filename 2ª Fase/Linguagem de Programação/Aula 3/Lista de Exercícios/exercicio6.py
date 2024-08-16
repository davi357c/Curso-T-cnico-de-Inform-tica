tuplaAleatoria = "casa", "cozinha", "gargarejo", "pilantra", "conversa", "inteligencia"
vogais = "a", "e", "i", "o", "u"
for v in tuplaAleatoria:
    print(f"\nPalavra --> {v}\nConsoantes:\n")
    for x in v:
        if x in vogais:
            print(x)

