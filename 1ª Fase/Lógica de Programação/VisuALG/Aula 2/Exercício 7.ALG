Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2024
Var
// Seção de Declarações das variáveis 
   nome: caracter
   idade: inteiro
   peso, altura, IMC: real
   
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   escreva("Qual seu nome? ")
   leia(nome)
   escreva("Qual sua idade? ")
   leia(idade)
   escreva("Qual seu peso? ")
   leia(peso)
   escreva("Qual sua altura? ")
   leia(altura)
   IMC <- peso/(altura*altura)
   escreva("Seu IMC é de ", IMC)
   
Fimalgoritmo