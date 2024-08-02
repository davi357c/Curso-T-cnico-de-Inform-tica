nome, senha = input(f'Qual o seu nome?'), input(f'Qual sua senha?')
while nome==senha:
    print(f'Sua senha não pode ser igual ao seu nome. Faça novamente:')
    nome, senha = input(f'Qual o seu nome?'), input(f'Qual sua senha?')
print(f'Ok.')