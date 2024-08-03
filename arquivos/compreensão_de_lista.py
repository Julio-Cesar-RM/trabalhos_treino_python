# numeros = [1,35,6,7,3,3,4]

# quadrados = list(map(lambda num: num**2, numeros))

# print(quadrados)

#========================================

#usando compreensão de listas

# numeros = [1,12,354,354,2,5,23]

# quadrados = [num**2 for num in numeros]

# print(quadrados)

# pares = [i for i in range(11) if i%2==0]
# print(pares)

#===========================================
alfabeto = 'Alberto Sanches'
vogais = [v for v in alfabeto if v in 'aeiouAEIOU']
print(vogais)