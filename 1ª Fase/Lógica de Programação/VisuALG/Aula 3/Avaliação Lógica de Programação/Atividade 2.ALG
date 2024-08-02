Algoritmo "Atividade 2"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Davi Camilo Caetano / 1137
// Data atual  : 21/03/2024
Var
// Seção de Declarações das variáveis 
nome, ce: caracter
idade: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Qual seu nome? ")
leia(nome)

escreva("Qual sua idade? ")
leia(idade)

escolha (idade)

caso 0 ate 16
     ce:="não votante"
     
caso 17 ate 18
     ce:="eleitor facultativo"
     
caso 18 ate 65
     ce:="eleitor obrigatório"
     
outrocaso
         ce:="eleitor facultativo"
         
fimescolha
     
escreva("Olá, ", nome,", atualmente você é um ", ce,"!")

Fimalgoritmo