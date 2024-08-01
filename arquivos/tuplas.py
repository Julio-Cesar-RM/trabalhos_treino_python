# permite armazenar dados igual as listas, porém elas são imutáveis

# tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# tupla[1] = 4 ==> erro
# print(tupla)
# print(type(tupla))

# halogenios = ('F', 'Cl', 'Br', 'I', 'At')
# gases_nobres = ('He','Ne','Ar','Xe','Kr','Rn')
# print(halogenios)

# print(len(halogenios))

# print(halogenios[2])

# #concatenar:

# elementos = halogenios+gases_nobres
# print(elementos)

#=======================================
# contar itens repetidos

# t1 = (1,2,3,3,3,4,5,6,6,7,7,7,7,7,8,8,9)
# print(t1.count(3))
# print(t1.count(7))
#======================================
#mostrar itens específicos
# t1 = (1,2,3,3,3,4,5,6,6,7,7,7,7,7,8,8,9)
# print(t1[0:3])
# print(3 in t1)
# print(sum(t1))
# print(max(t1))
# print(min(t1))
# =======================================
# qualquer ação como append, pop, sort, reverse, etc, que 
# altere a organização ou os itens de uma tupla, dão erro

#==========================================
#criar lista a partir de uma tupla

gases_nobres = ('He','Ne','Ar','Xe','Kr','Rn')
lista_gases_nobres = list(gases_nobres)
print(type(lista_gases_nobres))

print(sorted(gases_nobres)) # esse modo não altera a tupla, por isso eu consigo apenas mostrar ela
# em ordem alfabética, mas sem alterar sua ordem real
print(gases_nobres)

print(gases_nobres.sort) # já esse método, por alterar a composição real da tupla, não é
# possível utilizá-lo