var = 'Olá Mundo'
#Pegar carac espec:
print(var[2])
print(var[-3])

# Fatiamento - var[inicio:fim:passo]
# início é índice que inicia. Por padrão, é 0.
# fim é até qual caracter se pretende pegar o texto. Padrão é o último
# passo = 1 escreve todos os dígitos (padrão); 2 escreve 1 e pula 1; 3 escreve 2 e pula 1; ...
# inicia no índice 2 e finaliza no índice 4 (exclui o 5)
print(var[2:5])
# inicia no índice 0 e finaliza em 4 (exclui o 5)
print(var[:5])
# inicia no índice 6 e vai até o final
print(var[6:])

# Obter o tamanho da string (quantos caracteres) - função len (abreviatura de lenght)
print(len(var))
print(len(var[2:5]))

print(var[0:9:3])
print(var[1:9:3])
print(var[6:9:2])
#Números negativos invertem a string e funcionam similar à quantidadede casas normal
#Inicia-se no primeiro dígito de trás para frente (-1) e vai até o último
print(var[-1:-10:-1])
print(var[-1:-10:-2])

print(var[::-1])
