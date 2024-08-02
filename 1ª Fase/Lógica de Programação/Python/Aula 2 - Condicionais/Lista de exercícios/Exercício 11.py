nome = input(f'Qual seu nome?')
nh = float(input(f'Qual o seu número de horas trabalhadas?'))
vh = float(input(f'Qual o seu valor da hora trabalhada?'))
print(f'Com o desconto do INSS seu salário final ficará de {(nh*vh)/0.02:.2f}')