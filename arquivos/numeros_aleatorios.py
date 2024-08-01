import random

#sortear um valor aleatorio inteiro entre os que voce selecionar

# print('Quantos números aleatórios você quer gerar?')
# quant = int(input('Digite: '))
# print('Qual o número de início?')
# inicio = int(input('Digite: '))
# print('Qual o número final?')
# final = int(input('Digite: '))
# for c in range(quant):
#     ordem = 1
#     valor = random.randint(inicio, final)
#     print(f'Valor {ordem}: {valor}')
#     ordem += 1
# print('\n Fim.')

#===========================================================
#selecionar um valor com muitas casas decimais aleatorio entre 0 e 1, nao tem parametro.

# valor = random.random()
# print(f'Número gerado: {round(10*valor, 2)}')

#===========================================================
#selecionar um valor com muitas casas decimais aleatorio dentro do parametro que vc escolher.

# valor = random.uniform(1, 100)
# print(round(valor, 4))

#o 'round' arredonda o valor para a quantidade de casas decimais que escolher.
#===========================================================

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#no primeiro método 'choice', é selecionado um numero de uma lista aleatoriamente

# n = random.choice(lista)
# print(f'O valor selecionado foi: {n}')

#no segundo método 'sample' é selecionado uma quantidade n de valores de uma lista de maneira aleatória.

# n = random.sample(lista, 3)
# print(f'Os 3 valores selecionados foram: {n}')

#=============================================================

#embaralhar

print(f'Lista em ordem (original): {lista}')

random.shuffle(lista)

print(f'Lista em ordem (original): {lista}')
