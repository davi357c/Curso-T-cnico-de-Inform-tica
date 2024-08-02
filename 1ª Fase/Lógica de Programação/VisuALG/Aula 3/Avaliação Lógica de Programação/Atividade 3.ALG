Algoritmo "Atividade 3"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Davi Camilo Caetano / 1137
// Data atual  : 21/03/2024
Var
// Seção de Declarações das variáveis 
nome, IMC: caracter
peso, altura, calculo: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Qual seu nome? ")
leia(nome)

escreva("Qual sua altura? ")
leia (altura)

escreva("Qual seu peso? ")
leia(peso)

calculo:=peso/(altura*altura)

escolha(calculo)

caso 0 ate 18.5
     IMC:="abaixo do peso"

caso 18.5 ate 25
     IMC:="com peso normal"
     
caso 25 ate 30
     IMC:="acima do peso"
     
outrocaso
         IMC:="obeso"

fimescolha
     
escreva("Olá, ", nome,", seu IMC é de", calculo," e você está ", IMC,".")

Fimalgoritmo