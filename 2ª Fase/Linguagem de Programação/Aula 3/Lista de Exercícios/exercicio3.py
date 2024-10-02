from random import *
tuplaNumeros = ()
for v in range(5):
    tuplaNumeros += (randint(0, 1000),)
print(f"O maior número da tupla é {max(tuplaNumeros)} e o menor é {min(tuplaNumeros)}")

