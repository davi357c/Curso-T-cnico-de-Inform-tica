Algoritmo "Exerc�cio 4"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2024
Var
// Se��o de Declara��es das vari�veis 
   nome, produto: caracter
   quantidade: inteiro
   preco, precofinal: real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   escreva("Digite seu nome ")
   leia(nome)
   escreva("Qual produto pegou? ")
   leia(produto)
   escreva("Quantos pegou? ")
   leia(quantidade)
   escreva ("Qual o pre�o individual? ")
   leia(preco)
   precofinal<-quantidade*preco
   escreva("Sua compra de", quantidade," ", produto," ficou num total de", precofinal,", ",nome,"!")
   
Fimalgoritmo