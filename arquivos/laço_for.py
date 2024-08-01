# palavra = '12345'

# for letra in palavra:
#     print(letra)

# for i in range(1, 11, 2):
#     print (i)

pedras = ('rubi','esmeralda', 'quartzo','diamante','turmalina')

#nao quero que quartzo aparece

for i in pedras:
    if i == 'quartzo':
        continue
    print(i)