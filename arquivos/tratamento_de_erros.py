def div(k,j):
    return round(k/j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = float(input('Digite um número: '))
            n2 = float(input('Digite outro número: '))
            break 
        except ValueError:
            print('Ocorreu um erro de digitação, tente novamente.')
    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print('Não é possível dividir por zero.')
    except:
        print('Ocorreu um erro desconhecido.')
    else:
        print(f'O resultado foi: {r}')
    finally:
        print('\nFim do programa.')