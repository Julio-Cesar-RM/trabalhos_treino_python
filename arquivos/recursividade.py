def fatorial(j):
    if j == 0 or j == 1:
        return 1
    else:
        return j * fatorial(j - 1)
    
while True:
    try:
        x = int(input('Digite um número para calcular o seu fatorial: '))
        resposta = fatorial(x)
    except RecursionError:
        print('\nO número fornecido é muito grande ou negativo, tente novamente.\n')
    except ValueError:
        print('\nDigite um valor válido.\n')
    else:
        print(f'O fatorial de {x} é igual a: {resposta}.')
        break