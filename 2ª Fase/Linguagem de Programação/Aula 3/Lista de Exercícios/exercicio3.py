import random as rm
tuplaNumeros = ()
for v in range(5):
    tuplaNumeros += (rm.randint(0, 1000),)
print(f"O maior número da tupla é {max(tuplaNumeros)} e o menor é {min(tuplaNumeros)}")

