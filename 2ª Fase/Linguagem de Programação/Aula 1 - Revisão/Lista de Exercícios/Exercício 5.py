produto = input('Qual o produto escolhido? ')
quantia = int(input('Quantos você pegou? '))
preco = int(input('Qual o preço do produto? '))
forma = int(input('Qual será a forma de pagamento?\n\n1 - À vista em dinheiro recebe 10% de desconto\n2 - À vista no cartão de crédito, recebe 5% de desconto\n3 - Em duas vezes, preço normal sem juros\n4 - Em três vezes, preço normal mais juros de 5% acréscimo\n'))
while forma not in [1, 2, 3, 4]:
    forma = int(input('\nEscreva um valor válido.\nQual será a forma de pagamento?\n\n1 - À vista em dinheiro recebe 10% de desconto\n2 - À vista no cartão de crédito, recebe 5% de desconto\n3 - Em duas vezes, preço normal sem juros\n4 - Em três vezes, preço normal mais juros de 5% acréscimo\n'))
calculo = quantia * preco
if forma == 1:
    precoFinal = calculo * 0.9
elif forma == 2:
    precoFinal = calculo * 0.95
elif forma == 3:
    precoFinal = calculo
else:
    precoFinal = calculo * 1.05
print(f'O preço final é de: R$ {precoFinal:.2f}')