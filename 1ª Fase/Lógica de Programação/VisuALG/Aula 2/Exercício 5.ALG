Algoritmo "Exercício 5"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2024
Var
// Seção de Declarações das variáveis 
   nome, cargo: caracter
   salario, aumento: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   escreva("Qual seu nome? ")
   leia(nome)
   escreva("Qual seu cargo? ")
   leia(cargo)
   escreva("Quanto você ganha? ")
   leia(salario)
   aumento <- salario*1,05
   escreva("Olá, ", nome,", você receberá um aumento de 5%, indo de ", salario," para ", aumento,"!")

Fimalgoritmo