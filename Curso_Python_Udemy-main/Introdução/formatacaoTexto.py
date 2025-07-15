nome = 'Lucas B'
altura = 1.8
peso = 95

imc = peso/altura**2

# FORMATAÇÃO TIPO 1
texto = f'{nome} tem {peso:.1f} kg e {altura:.2f} m'
print(texto + "\n")

print(f'SEM VARIÁVEL - {nome} tem {peso :.1f} kg e {altura :.2f} m. \nPortanto, seu imc é {imc :.4f}')


# FORMATAÇÃO TIPO 2
# Outra opção de formatação: - adicionar o format após a variável
a = 'AAA'
b = 'BB'
c = 5
var1 = ''.format(a, b, c)
print (var1)

# cada chave referencia um valor do format
var1 = 'a={} b={} c={:.3f}'.format(a, b, c)
print(var1)

var2 = 'a={} b={} c={:.5f}'
print('print format ' +  var2.format(a, b, c))


# FORMATAÇÃO TIPO 3
var3 = 'a={1} b={0} c={teste:.5f} IMC = {1}'
formatoVar3 = var3.format(
    b, a, teste = imc
)
print(formatoVar3)
# Após alguma variável receber um parâmetro, todas as outras também deverão receber As anteriores a ela não precisam

# FORMATAÇÃO TIPO 4
var4 = 'a={1} b={0} c={2} IMC = {1}'
formatoVar4 = var4.format(
    b, a, imc
)
print(formatoVar3)

# O código abaixo resultará em erro, devido ao excesso de variáveis.
# var1 = 'a={} b={} c={:.3f} {}'.format(a, b, c)
# print (var1)

# INTERPOLAÇÃO - Outro tipo de formatação

nome1 = 'John Smith'
preco = 1000.897157
strImpressao = '%s, o preço é R$ ' % nome1
print(strImpressao)

strImpressao = '%s, o preço é R$ %.2f' % (nome1, preco)
print(strImpressao)

# Utilizar converter valor para hexadecimal:
# X para maiúsculo, x para minúsculo
print('o hexadecimal de %d é %x' % (15,15) )
#O 010 antes do X indica quantas casas deve possuir (10) e oque deve aparecer nas casas anteriores, neste caso, 0
print('o hexadecimal de %d é %010X' % (14,14) )
# O 010 antes do X indica quantas casas deve possuir (10) e oque deve aparecer nas casas anteriores, neste caso, " "
print('o hexadecimal de %d é %10X' % (14,14) )


#
# F STRINGS
#

# Formatar textos com largura fixa:
# > desloca para a direita, inserindo os caracteres à esquerda
# < desloca para a esquerda, inserindo os caracteres à direita
# ^ meio dos caracteres
variavel = 'ABC'
print(f'{variavel: >10}')
print(f'{variavel:a>10}')
print(f'{variavel:\n>10}')
print(f'{variavel:->10}')
print(f'{variavel:$>10}')

# O caracter localizado após os dois pontos será o caracter adicionado até completar
# a quantidade desejada de caracteres    
print(f'{variavel:1<10}')
print(f'{variavel:1^10}')

# Explicando o código
# primeiro 0 após os dois pontos: caracter que será preenchido para completar o total de casas
# + é utilizado para representar números positivos com o sinal na frente
# 10 é o total de casas que deve possuir o valor com todas as especificações
# 0.1 é a quantidade de casas após a vírgula
# = força o + a estar antes de todos os números, seguido pelos 0.        
print(f'{1000.4587535:0=+10,.1f}')

#Para hexadecimal:
print(f'o hexadecimal de 1500 é {1500:08X}')

#CAPITALIZE - Torna a primeira letra da string Maiúscula
print(nome.capitalize())
#CASE das letras
print(nome.lower())
print(nome.upper())