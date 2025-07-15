# Para variáveis que não devem ser mudadas - valor deve permanecer constante
# Por convenção, são utilizadas LETRAS MAÍUSCULAS PARA DEFINÍ-LAS.
# Exemplo

# velocidade pode ser alterada. A velocidade do radar deve se manter a mesma.
velocidade = 50
RADAR1 = 60


var1 = 'teste'
var2 = 2
print(var1, var2, sep=" 0")

nome = 'pedro'
idade = 22
maior_de_idade = 22>18

print(maior_de_idade)

print(int(7.7+10))

# VARIÁVEIS DIFERENTES, COM VALORES ATRIBUÍDOS IGUAIS SÃO ARMAZENADOS NO MESMO ESPAÇO DE MEMÓRIA,
# A FIM DE OTIMIZAR O CÓDIGO E ESPAÇO NECESSÁRIO. EXEMPLO:
var4 = 'a'
var5 = 'a'
print(id(var5))
print(id(var4))

# FLAGS - variáveis de apoio para saber se algo foi validado. EXEMPLO:
condicao = False
passouIf = None

# IS e IS NOT - usado para tipo, valor ou identidade; NONE - caso não tenha valor
if condicao:
    passouIf = True
    print('Passou no if')
else:
    print('Não passou')
print(passouIf, passouIf is None)
# Também pode ser utilizado como print(passouIf, passouIf == None)
print(passouIf, passouIf is not None)
# Também pode ser utilizado como print(passouIf, passouIf != None)
# EM PYTHON, AS VARIÁVEIS SÃO IMUTÁVEIS - Não podem ser alteradas diretamente,
# somente se for atribuído um novo valor

# Atribuindo novo valor
texto = 'ABC'
texto = 'DEF'
#Não é possível fazer: - Imutável
# texto[2] = 't'
