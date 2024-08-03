#funções lambda / anônimas

# quadrado = lambda x: x**2

# for i in range(1,11):
#     print(quadrado(i))

# par = lambda y: (y % 2) == 0

# print(f'O numéro oito é par? {par(8)}')
# print(f'O numéro nove é par? {par(9)}')

#==================================

#função map() ===> aplica uma função em varios valores

# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x * 2, num))
# print(dobro)

# palavras = ['python', 'é', 'uma', 'linguagem', 'de', 'programação']

# maiusculas = list(map(str.upper, palavras))
# print(maiusculas)

#=======================================

#função filter() ===> se o resultado da função feita para cada item iterado for false, ele retira o item

# def numeros_pares(n):
#     return n % 2 == 0

# numeros = [1,2,3,4,5,6,7,8,9,10]

# num_par = list(filter(numeros_pares, numeros))

# print(num_par)

# numeros_impares = lambda x: x % 2 != 0

# num_impar = list(filter(numeros_impares, numeros))

# print(num_impar)

#======================================================

