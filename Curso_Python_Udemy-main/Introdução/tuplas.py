# Tuplas são mais eficientes que listas, porém, são imutáveis.

lista = ['Karina', 'Luana', 'Inacio']
tupla = 'Karina', 'Luana', 'Inacio'
# Não permite fazer tupla[0] = 'A', pois não é permitido alterá-la.
#porém, permite utilizar o índice normalmente
print(tupla[1])

# É possível também fazer a conversão de lista para tupla
nomes = tuple(lista)
print(lista)
# Também é possível reverter
nomes = list(nomes)