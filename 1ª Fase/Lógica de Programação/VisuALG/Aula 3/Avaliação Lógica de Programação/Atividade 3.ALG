Algoritmo "Atividade 3"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Davi Camilo Caetano / 1137
// Data atual  : 21/03/2024
Var
// Se��o de Declara��es das vari�veis 
nome, IMC: caracter
peso, altura, calculo: real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreva("Qual seu nome? ")
leia(nome)

escreva("Qual sua altura? ")
leia (altura)

escreva("Qual seu peso? ")
leia(peso)

calculo:=peso/(altura*altura)

escolha(calculo)

caso 0 ate 18.5
     IMC:="abaixo do peso"

caso 18.5 ate 25
     IMC:="com peso normal"
     
caso 25 ate 30
     IMC:="acima do peso"
     
outrocaso
         IMC:="obeso"

fimescolha
     
escreva("Ol�, ", nome,", seu IMC � de", calculo," e voc� est� ", IMC,".")

Fimalgoritmo