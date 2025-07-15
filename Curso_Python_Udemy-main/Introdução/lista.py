# Em outras linguagens de programação, é utilizado chamado de array
# É um tipo mutável
# Suporta diversos valores de qualquer tipo

lista = []
# Caso a lista esteja vazia, seu bool é falsy
print(bool(lista))
print(lista, type(lista))

lista = [123, True, 'Lucas B', 1.2, []]
print(lista)

lista[2] = False
print(lista)

# Para adicionar coisas ao final da lista:
lista.append('Lucas B')
lista.append(56)
print(lista)

# Funciona como uma fila - FIFO - pop remove o último valor adicionado
# Pop retorna e remove o último valor
valorRemovido = lista.pop()
# Para remover um item específico da lista - recomendado somente para listas pequenas
valorMeio = lista.pop(2)
print(lista, f'removidos: final: {valorRemovido}, meio: {valorMeio}')

# del deleta o valor da lista com índice respectivo
# Índice -1 é o último inserido
del lista[-1]

# Clear limpa a lista - cria uma nova
lista.clear()

# Ao utilizar um insert, caso o último item seja maior que o maior índice da lista, é desconsiderado o índice e insere ao final
lista.insert(0,5)
# Insert insere valor na lista. Pode receber um parâmetro de

# + é utilizado para concatenar as listas
listaA = [1, 2, 3]
listaB = [4, 5, 6]
listaC = listaA + listaB + [7, 8, 9]
print(listaC)

# Também é possível fazer da seguinte forma:
listaD = listaA.extend(listaB)
print(listaA)
# Extend afeta diretamente a lista A e não retorna valor, então a lista D fica nula.
print(listaD)

# CUIDADOS A SEREM TOMADOS COM OS DADOS MUTÁVEIS
# Para dados imutáveis, é possível trocar a referência
nome = 'Lucas'
novoNome = nome
nome = 'Lucas B'
# É criado um novo endereço na memória.

# Para listas, entretanto, a nova variável aponta para o mesmo endereço de memória da variável anterior
lista1 = ['Lucas', 'Karina']
lista2 = lista1

lista1[0] = 'abc'
print(lista2)

# O certo é fazer: 
lista2 = lista1.copy()