Algoritmo "Exercício 4"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2024
Var
// Seção de Declarações das variáveis 
   nome, produto: caracter
   quantidade: inteiro
   preco, precofinal: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   escreva("Digite seu nome ")
   leia(nome)
   escreva("Qual produto pegou? ")
   leia(produto)
   escreva("Quantos pegou? ")
   leia(quantidade)
   escreva ("Qual o preço individual? ")
   leia(preco)
   precofinal<-quantidade*preco
   escreva("Sua compra de", quantidade," ", produto," ficou num total de", precofinal,", ",nome,"!")
   
Fimalgoritmo