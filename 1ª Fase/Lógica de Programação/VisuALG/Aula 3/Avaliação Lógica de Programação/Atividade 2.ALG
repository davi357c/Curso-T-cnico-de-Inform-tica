Algoritmo "Atividade 2"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Davi Camilo Caetano / 1137
// Data atual  : 21/03/2024
Var
// Se��o de Declara��es das vari�veis 
nome, ce: caracter
idade: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreva("Qual seu nome? ")
leia(nome)

escreva("Qual sua idade? ")
leia(idade)

escolha (idade)

caso 0 ate 16
     ce:="n�o votante"
     
caso 17 ate 18
     ce:="eleitor facultativo"
     
caso 18 ate 65
     ce:="eleitor obrigat�rio"
     
outrocaso
         ce:="eleitor facultativo"
         
fimescolha
     
escreva("Ol�, ", nome,", atualmente voc� � um ", ce,"!")

Fimalgoritmo