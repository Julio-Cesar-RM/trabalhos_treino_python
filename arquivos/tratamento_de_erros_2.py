#uso do 'raise'

import math

# if __name__=='__main__':
#     while True:
#         try:
#             num = float(input('Digite um número positivo: '))
#             if num < 0:
#                 raise ArithmeticError # forço ele a dar um erro, antes do erro ocorrer, para corrigir.
#         except ArithmeticError:
#             print('Digite um número positivo, pois não existe raiz de negativos.')
#         except ValueError:
#             print('Digite um número válido.')
#         else:
#             print(f'O resultado da raiz de {num} é igual a: {round(math.sqrt(num), 2)}')
#             break

#==============================================

#criando as minhas próprias exceções

class NumeroNegativoError(Exception):
    def __ini__(self):
        pass

if __name__=='__main__':
    while True:
        try:
            num = float(input('Digite um número positivo: '))
            if num < 0:
                raise NumeroNegativoError # forço ele a dar um erro, antes do erro ocorrer, para corrigir.
        except NumeroNegativoError:
            print('Digite um número positivo, pois não existe raiz de negativos.')
        except ValueError:
            print('Digite um número válido.')
        else:
            print(f'O resultado da raiz de {num} é igual a: {round(math.sqrt(num), 2)}')
            break
