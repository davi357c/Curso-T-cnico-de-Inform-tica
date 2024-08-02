Algoritmo "Atividade 4"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Davi Camilo Caetano / 1137
// Data atual  : 21/03/2024
Var
// Seção de Declarações das variáveis 
celsius, tf: real
T, tip: caracter

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Qual a temperatura em celsius? ")
leia(celsius)

escreval("Para qual vocêquer converter? Fahrenheit, Kelvin ou Réaumur? ")
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
     tip:="Réaumur"

fimescolha

escreva("A temperatura em ", tip," é de", tf)

Fimalgoritmo