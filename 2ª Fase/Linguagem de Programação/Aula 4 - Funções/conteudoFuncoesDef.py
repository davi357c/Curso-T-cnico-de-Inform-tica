""" def primeiraFuncao():
    print("Sejam bem vidos a aula de LP!")
primeiraFuncao() """

""" def cores():
    cor1 = input("Mim diga a primeira cor: ")
    cor2 = input("Mim diga a segunda cor: ")
    print(f"As cores escolhidas são {cor1} e {cor2}")
cores() """

""" def pessoa(nome):
    print(f'Seja bem vindo {nome}')
pessoa("slabao") """

""" def somar(a, b):
    print(f'A soma dos valores é {a + b}')
somar(10 + 13) """

""" def somar(a = 0, b = 0):
    print(f'A soma dos valores é {a + b}')
valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))
somar(valor1) """

""" def somar(*args):
    print(args)
    s = 0
    for v in args:
        s += v
    print(f'A soma dos valores é {s}')
somar(1, 2, 3, 4, 5, 7, 6) """

""" def somar(*args):
    s = sum(args)
    print(f'A soma dos valores é {s}')
somar(1, 2, 3, 4, 5, 7, 6) """

""" def pessoas(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave} --> {valor}")
nome = input("Qual seu nome?")
idade = float(input("Qual sua idade?"))
endereco = input("Qual sua endereço?")
pessoas(nome=nome, idade=idade, endereço=endereco) """

""" def somar(a, b):
    s = a + b
    return s
print(somar(12, 12)) """


# acessar return com 2 valores e convertelos em um

""" def somar(a, b):
    s = a + b
    m = a * b
    return s, m
soma, multiplicacao = somar(12, 12)
print(soma);
print(multiplicacao) """


# acessar com return

""" def par(number):
    if number % 2 == 0:
        return "Esse valor é par"
    if number % 2 == 1:
        return "Esse valor é ímpar"
print(par(11))
print(par(12)) """


# acessar com global

""" def somar(a, b):
    global s
    s = a + b
print(somar(12, 12))
print(s) """


# tudo numa linha

""" def somar(a, b): return (a + b) """

# importa os carai tudo
""" from datetime import *
print(datetime.today()) """

# importa só um
""" from time import sleep
print(f"Cadastrando dados...")
sleep(2)
print("Dados Cadastrados!") """

from math import *

raiz = sqrt(121)
print(raiz)

potencia = pow(11)
print(potencia)

fatorial = pow(11)
print(fatorial)