#escopo global e local

# var_global = 'curso completo de python'

# def escreve_texto():
#     var_local = 'Júlio César'
#     print(f'Variável global: {var_global}')
#     print(f'Variável local: {var_local}')

# print(escreve_texto())
# print(f'Variável global: {var_global}')
# print(f'Variável local: {var_local}') #erro, pois é uma variável local

#================================================
#serão mostrados valores diferentes, pois a var global não se alterará com a função

# var = 'bancos de setas'

# def escreve():
#     var = 'bancos de dados'
#     print(var)

# escreve()
# print(var)

#para realmente acessar e mudar uma var global em uma função, temos que usar este método:
#neste caso, a var foi realmente alterada, e aparecerá o mesmo valor
var = 'bancos de setas'

def escreve():
    global var
    var = 'bancos de dados'
    print(var)

escreve()
print(var)
