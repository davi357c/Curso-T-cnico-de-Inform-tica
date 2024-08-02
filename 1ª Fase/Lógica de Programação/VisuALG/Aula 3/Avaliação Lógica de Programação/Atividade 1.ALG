Algoritmo "Atividade 1"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Davi Camilo Caetano / 1137
// Data atual  : 21/03/2024
Var
// Seção de Declarações das variáveis 
produto, tp: caracter
quantidade: inteiro
preco, pf, calculo, desconto: real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Qual o produto? ")
leia(produto)

escreva("Quantos pegou? ")
leia(quantidade)

escreva("Qual o preço? ")
leia(preco)

escreval
escreval("Qual o tipo de pagamento? À vista em dinheiro, à vista em cartão de crédito, em duas vezes ou em três vezes?")
escreval
escreval("À vista em dinheiro = 10% de desconto")
escreval("À vista em cartão de crédito = 5% de desconto")
escreval("Em duas vezes = preço normal")
escreval("Em três vezes = 5% de juros")
escreval
escreva("Responda em (VD, VC, DV, TV) -> ")
leia(tp)

escolha(tp)

caso "VD"
     desconto:=0.9
     
caso "VC"
     desconto:=0.95
     
caso "DV"
     desconto:=1
     
caso "TV"
     desconto:=1.05
     
fimescolha

calculo:=quantidade*preco*desconto

escreva("O preço final de sua compra é de ", calculo," reais!")

Fimalgoritmo