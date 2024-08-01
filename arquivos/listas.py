#lista: representa uma sequência de valores, que pode ser modificada.

# notas = [4.5, 5, 10, 9.5, 7]
# print(notas)

#=======================
# concatenar listas

# n1 = [1,2,3,4,5]
# n2 = [6,7,8,9,10]
# lista = n1 + n2
# print(lista)

#=========================
# acessar valores

# n1 = [1,2,3,4,5]
# print(n1[0])
# print(n1[-1])
#==========================
# alterar valores de lista

# n1 = [1,2,3,4,7,5]
# print(n1)
# n1[4] = 4
# print(n1)
#===========================
# acessar valores sequenciais da lista
# mostra apenas do valor inicial, ate a posição -1 que vc pos.

# n1 = [1,2,3,4,5]
# print(n1[0:3])
#=============================
# quantida de valores de uma lista

# n1 = [1,2,3,4,5]
# print(len(n1))
#=============================
#ordenar lista em ordem crescente ou decrescente

# n1 = [4,1,6,2,7,2,7,2,1,6]
# print(sorted(n1))

# print(sorted(n1, reverse=True))
#=================================
# somar todos os valores de uma lista. Encontrar maior valor, e menor valor

# n1 = [1,3,5,1,5,6]
# print(sum(n1))
# print(min(n1))
# print(max(n1))
#====================================
#manipular listas

#adicionar itens no seu final:
# valores = [1,2,4,5]
# valores.append(2)
# print(valores)

# #tirar o ultimo elemento da lista, ou de alguma posilçao específica:
# valores.pop()
# print(valores)

# valores.pop(0)
# print(valores)

# #inserir valores no meio de uma lista (primeiro vem a posição, e depois o valor em questão)
# valores.insert(0, 12)
# print(valores)
#=====================================
# verificar se há um valor na lista (true or false)

# lista = [1,2,3,4,5,6,7,8,9]
# print(10 in lista)
# print(4 in lista)
#======================================
planetas = list()
planetas.append('Netuno')
planetas.append('Urano')
planetas.append('Saturno') 
planetas.append('Marte')
planetas.append('Vênus')
planetas.append('Mercúrio')
for planeta in planetas:
    print(planeta)