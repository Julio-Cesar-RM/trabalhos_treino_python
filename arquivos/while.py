nome = None

while True:
    nome = input('Digite o seu nome ou \'x\' para parar: ')
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem vindo {nome}!')