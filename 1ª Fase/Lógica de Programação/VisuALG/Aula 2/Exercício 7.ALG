Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2024
Var
// Se��o de Declara��es das vari�veis 
   nome: caracter
   idade: inteiro
   peso, altura, IMC: real
   
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
   escreva("Qual seu nome? ")
   leia(nome)
   escreva("Qual sua idade? ")
   leia(idade)
   escreva("Qual seu peso? ")
   leia(peso)
   escreva("Qual sua altura? ")
   leia(altura)
   IMC <- peso/(altura*altura)
   escreva("Seu IMC � de ", IMC)
   
Fimalgoritmo