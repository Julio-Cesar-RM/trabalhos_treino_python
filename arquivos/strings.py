# nome = 'Roberto'
# letra = nome[2]
# print(letra)

# print(len(nome))

# curso = 'curso de python'
# aluno = 'Geraldo'
# print(curso + ' ' + aluno)

#============================
# frase = 'Vamos aprender python hoje'
# palavras = frase.split() # separa cada palavra em um item de uma lista
# print(palavras)
# print(palavras[1])

# for palavra in palavras:
#     print(palavra)

# for letra in frase:
#     print(letra)

# print(frase[0:5])
# print(frase[6:15]) 

#=============================
# email = input('Digite seu email: ')
# arroba = email.find('@') # encontra o local/índice do caracter em questão
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(f'voce é o usuário: {usuario}')
# print(f'seu dominio é: {dominio}')
#===============================

# produtos = 'carbonato de sodio e oxido de zinco'
# print('sodio' in produtos) #true
# print('magnesio' in produtos) #false

# item = 'hipoclorito'
# posicao = item.find('clor')
# print(posicao)
# posicao = item.find('flor')
# print(posicao) # o resultado aparecerá '-1' o que quer dizer que nao tem aquela substring
#=========================================

# objeto = 'galáxia esPiral M31'
# print(objeto.upper()) #texto todo em maiúsculo
# print(objeto.lower()) #texto todo em minúsculo 
# print(objeto.capitalize()) #texto com somente a primeira letra em maiúsculo
# print(objeto.title()) #texto com cada primeira letra de cada palavra em maiúsculo

#=========================================

# suplemento = 'cloreto de magnesio'
# novo_suplemento = suplemento.replace('magnesio','zinco') #criei uma nova string, e usei o metodo replace para
# # com o primeiro argumento selecionar o que eu quero trocar, e com o segundo argumento, dizer o que eu quero 
# # no lugar do anterior.
# print(suplemento)
# print(novo_suplemento)

#==========================================
#tirar espaços em branco no inicio ou fim
# frase = '   ola mundo, tudo bem?   '
# print(frase)
# print(frase.lstrip()) #tira espaços da esquerda
# print(frase.rstrip()) #tira espaços da direita
# print(frase.strip()) #tira espaços dos dois lados

#==================================================
#alinhamento de texto para exibição

# fruta = 'abacate'
# print(fruta)
# print(fruta.rjust(20)) #coloco N espaços e depois a fruta
# print(fruta.center(20)) #coloco N espaços e a fruta fica entre eles/ no meio deles
# print(fruta.ljust(20)) #coloco primeiro a fruta e depois N espaços depois dela
# print(fruta.ljust(20, '-')) #coloca no lugar de apenas 'espaços' o caracter escolhido na segunda posição
#======================================================
#prefixos e sufixos

# p = 'Bóson Treinamentos'
# print(p.startswith('Bó')) #é um resultado boleano que verifica se aquele item começa com o argumento dado ou não
# print(p.endswith('s')) #é um resultado boleano que verifica se o item termina com o argumento dado

#===========================================
#docstrings: documentar coisas, como funções

# texto = '''
# Docstring é uma espécie de documentação que podemos inserir dentro de um módulo
# função ou classe em python, entre outros locais. 
# Respeita deslocamento do texto e é multilinhas.
# '''
# print(texto)