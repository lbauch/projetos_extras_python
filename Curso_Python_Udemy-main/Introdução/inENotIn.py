#Strings em Python são iteráveis - é possível pegar item a item.

#Índice:          0  1  2  3  4
#Letra:           L  U  C  A  S
#Índice Negativo: -5 -4 -3 -2 -1

#As palavras possuem índices tanto positivos quanto negativos.

nome = "Lucas"
print(nome[2])
print(nome[-2])
print('--------------')
print("c" in nome)
print("cas" in nome)
print("cas0" in nome)
print('--------------')
print("c" not in nome)
print("cas" not in nome)
print("cas0" not in nome)

nome = input('Qual seu nome?\n')
encontrar = input('Oque deseja encontrar em seu nome?\n')
if encontrar in nome:
    print(f'{encontrar} encontrado em {nome}')
else:
    print(f'{encontrar} não encontrado em {nome}')