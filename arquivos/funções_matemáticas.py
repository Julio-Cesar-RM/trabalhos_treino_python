#funções internas:
# valores = [2,4,5,-4,0,23]
# print(max(valores))
# print(min(valores))

# a = -5
# b = 4
# print(abs(a)) # módulo
# print(pow(a, b)) # potenciação --> a elevado a b --> a^b

# c = 4.213125412312316474
# print(round(c, 2)) # arredondamento 

#==========================================
# usando import math
import math as m

x = 6
y = 45

raiz_quadrada = m.sqrt(x)
print(raiz_quadrada)
print(round(raiz_quadrada, 3)) # arredondamento padrão

print(m.ceil(raiz_quadrada)) # arredonda para o número inteiro maior

print(m.floor(raiz_quadrada)) # arredonda para o número inteiro menor

logaritmo = m.log10(y) # faz o log da base 10 de y
print(logaritmo)

print(m.pi) # número pi

fatorial = m.factorial(x) # calcula o fatorial de x '6'
print(fatorial)

#usando infinito:

print(x/ m.inf) # dividir algo por infinito, é igual a 0