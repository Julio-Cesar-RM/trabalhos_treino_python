print('\nDigite as suas cinco bebidas favoritas')
bebidas = list()

for i in range(5,0,-1):
    a = input(f'\nDigite a {i}º bebida favorita: ')
    bebidas.append(a)

print('-'*20)
print('\nSuas cinco bebidas favoritas em ordem alfabética são:\n')

bebidas.sort()
for i in bebidas:
    print('\t',i)
