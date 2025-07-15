lista = ['Karina', 'Luana', 'Inacio']
lista.append('Lucas')

listaEnumerada = enumerate(lista, start=1)
print(next(listaEnumerada))
# O valor enumerado vira uma tupla com o índice relativo ao item no primeiro índice da tupla e o valor no segundo índice da tupla

for item in enumerate(lista):
    a, b = item
    print(a, b)

#Também pode ser feito da seguinte forma:
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

# Cria uma tupla com (índice, valor) e repete para todos os indices da lista
