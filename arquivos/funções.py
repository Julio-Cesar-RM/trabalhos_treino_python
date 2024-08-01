# def mensagem():
#     print('Bóson Treinamentos')
#     print('Curso de Python')

# mensagem()

# #===============================

# def soma(a, b):
#     print(a + b)

# soma(1,5)

# #=============================
# def multi(x, y):
#     return x * y

# c = multi(5,6)
# print(c)

# #===========================

# def div(k, j):
#     if j != 0:
#         print(k/j)
#         return k/j
#     else:
#         print('impossível dividir por zero')

# div(5,0)

# #=============================

# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x**2)
#     return quadrados

# valores = [12,41,5,1,65,21]
# resultado = quadrado(valores)
# print(resultado)

#=================================
# def contar(n=10, caracter ='+'):
#     for i in range(n):
#         print(caracter)

# contar()

# contar(caracter='&')

# contar(n = 5, caracter = '@')

# contar(2,'-')

x = 5
y = 6
z = 3

def soma_mult(a,b,c = 0):
    if c == 0:
        return a*b
    else:
        return a+b+c
    
resultado = soma_mult(x, y)
print(resultado)

resultado = soma_mult(x,y,z)
print(resultado)