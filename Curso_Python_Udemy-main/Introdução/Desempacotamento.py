listaNomes = ['Karina', 'Luana', 'Inacio']
nome1, nome2, nome3 = listaNomes
print(nome1)

# Também pode ser feito da seguinte forma:
nome1, nome2, nome3 = ['Karina', 'Luana', 'Inacio']
print(nome2)

# Ao tentar desempacotar mais valores doque é possível atribuir, dá erro (too many values to unpack)
# nome1, nome2 = ['Karina', 'Luana', 'Inacio']

# Erro similar ocorre ao tentar desempacotar com mais variáveis, não sendo possível atribuir valor a todas
# nome1, nome2, nome3, nome4 = ['Karina', 'Luana', 'Inacio']

# Para não ocorrer este erro, é possível utilizar a seguinte forma:
nome1, *resto = ['Karina', 'Luana', 'Inacio']
print(nome1)
# O asterisco armazena todos os demais valores que não foram pegos
print(resto)

# Por convenção, variáveis que não serão utilizadas, somente é criado um _.
nome1, *_ = ['Karina', 'Luana', 'Inacio']

# Para pegar o 2ª nome:
_, nome2, *_ = ['Karina', 'Luana', 'Inacio']