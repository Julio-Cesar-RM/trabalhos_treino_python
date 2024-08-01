# elementos = {
#     'Z': 3,
#     'nome': 'Lítio',
#     'Grupo': 'Metais Alcalinos',
#     'Densidade':0.534
#     }

# print(f'Elemento: {elementos['nome']}')
# print(f'Densidade: {elementos["Densidade"]}')
# print(f'O dicionário Elementos possui: {len(elementos)} elementos')

# #atualizar, alterar dicionário ou excluir
# elementos['Grupo'] = 'alcalinos' #troquei 'metais alcalinos' por 'alcalinos'
# print(elementos)

# elementos['período'] = 2
# print(elementos)

# del elementos['período']
# print(elementos)

# #apagar todos os itens

# elementos.clear()
# print(elementos)

# #apagar o dicionario em si

# del elementos
# print(elementos) # vai dar um erro pq ele n existe mais

#===============================================
#vizualizar itens do dicionario
elementos = {
     'Z': 3,
     'nome': 'Lítio',
     'Grupo': 'Metais Alcalinos',
     'Densidade':0.534
     }
print(elementos.items())

for i in elementos.items():
    print(i)

print(elementos.keys()) #mostra so as chaves do dicionario

print(elementos.values()) #mostra so os valores

for i, j in elementos.items(): # mostra chave e valor juntos numa string
    print(f'{i}: {j}')
