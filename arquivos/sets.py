#itens n podem ser alterados, mas voce pode acrescentar mais

# planeta_anao = {'Plutao', 'Ceres','Eris', 'Haumea','Makemake'}
# print(planeta_anao)
# print(type(planeta_anao))
# print(len(planeta_anao))
# print('Ceres' in planeta_anao) #true
# print('Lua' in planeta_anao) #false

# for astro in planeta_anao:
#     print(astro.upper(), end=', ')

#===============================
#transformar lista em set

# astros = ['lua','venus','marte','lua','sirius']
# print(astros)

# astros_set = set(astros)

# print(astros_set) # em sets, os valures nao podem ser duplicados

#===================================
#comparações entre conjuntos 

astros1 = {'lua','venus','marte','lua','sirius'}
astros2 = {'lua','venus','marte','lua','sirius', 'júpiter'}
print(astros1 == astros2) #false

#uniao de conjuntos
print(astros1 | astros2)
print(astros1.union(astros2))

#interseção de conjuntos
print(astros1 & astros2)
print(astros1.intersection(astros2))

#diferença simetrica de conjuntos
print(astros1 ^ astros2)
print(astros1.symmetric_difference(astros2))

#adicionar elementos em conjuntos/sets
astros1.add('urano')
print(astros1)

#remover elementos em conjuntos
astros1.remove('lua')
print(astros1)
astros1.discard('marte')
print(astros1)

#eliminar um elemento aleatório do conjunto
astros1.pop()
print(astros1)

#limpar um conjunto inteiro
astros1.clear()
print(astros1)