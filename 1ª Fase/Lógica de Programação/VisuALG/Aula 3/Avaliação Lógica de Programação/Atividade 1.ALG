Algoritmo "Atividade 1"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Davi Camilo Caetano / 1137
// Data atual  : 21/03/2024
Var
// Se��o de Declara��es das vari�veis 
produto, tp: caracter
quantidade: inteiro
preco, pf, calculo, desconto: real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreva("Qual o produto? ")
leia(produto)

escreva("Quantos pegou? ")
leia(quantidade)

escreva("Qual o pre�o? ")
leia(preco)

escreval
escreval("Qual o tipo de pagamento? � vista em dinheiro, � vista em cart�o de cr�dito, em duas vezes ou em tr�s vezes?")
escreval
escreval("� vista em dinheiro = 10% de desconto")
escreval("� vista em cart�o de cr�dito = 5% de desconto")
escreval("Em duas vezes = pre�o normal")
escreval("Em tr�s vezes = 5% de juros")
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

escreva("O pre�o final de sua compra � de ", calculo," reais!")

Fimalgoritmo