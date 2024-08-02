remuneracao = float(input('Quando você ganha por hora? '))
tempo = int(input('Quantas horas você trabalhou este mês? '))
dinheiroBruto = remuneracao*tempo
print(f'\na) Seu salário bruto é de: R$ {dinheiroBruto:.2f}.')
print(f'b) R$ {dinheiroBruto*0.08:.2f} foi debitado do seu salário devido ao INSS.')
print(f'c) R$ {dinheiroBruto*0.05:.2f} foi debitado do seu salário devido ao sindicato.')
print(f'd) Seu salário líquido é de: R$ {dinheiroBruto - dinheiroBruto*0.11 - dinheiroBruto*0.08 - dinheiroBruto*0.05:.2f}.\n')