Algoritmo "Atividade 4"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Davi Camilo Caetano / 1137
// Data atual  : 21/03/2024
Var
// Se��o de Declara��es das vari�veis 
celsius, tf: real
T, tip: caracter

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreva("Qual a temperatura em celsius? ")
leia(celsius)

escreval("Para qual voc�quer converter? Fahrenheit, Kelvin ou R�aumur? ")
escreva("Responda em (F, K ou RE)")
leia(T)

escolha(T)

caso "F"
     tf:=celsius*1.8+32
     tip:="Fahrenheit"
     
caso "K"
     tf:=celsius+273.15
     tip:="Kelvin"

caso "RE"
     tf:=celsius*0.8
     tip:="R�aumur"

fimescolha

escreva("A temperatura em ", tip," � de", tf)

Fimalgoritmo