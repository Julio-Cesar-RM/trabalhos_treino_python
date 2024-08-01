# for cont_ex in range(1, 6):
#     print(f'\nRodada: {cont_ex}\n')
#     for cont_in in range(5, 0 , -1):
#         print(f'Valor: {cont_in}')
# print('\nfim dos laços')

import random

for a in range(1, 6):
    print(f'\nConjunto {a}:\n')
    for b in range(1, 6):
        num = random.randint(1, 100)
        print(num)