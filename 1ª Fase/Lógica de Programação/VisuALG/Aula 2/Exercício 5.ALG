Algoritmo "Exerc�cio 5"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2024
Var
// Se��o de Declara��es das vari�veis 
   nome, cargo: caracter
   salario, aumento: real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   escreva("Qual seu nome? ")
   leia(nome)
   escreva("Qual seu cargo? ")
   leia(cargo)
   escreva("Quanto voc� ganha? ")
   leia(salario)
   aumento <- salario*1,05
   escreva("Ol�, ", nome,", voc� receber� um aumento de 5%, indo de ", salario," para ", aumento,"!")

Fimalgoritmo