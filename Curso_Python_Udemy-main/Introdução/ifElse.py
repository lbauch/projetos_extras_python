entrada = input('Você quer entrar ou sair? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada =='sair':
    print('você saiu do sistema')
else:
    print('Opção inválida - Válidas: "Entrar" ou "Sair"')
print('FORA DAS CONDIÇÕES')

condicaoTrue = True
if condicaoTrue:
    print('cond true')
else:
    print('else') 


str1 = 'abcde'
str2 = 'abcde'

if(str1 == str2):
    print(True)
else:
    print(False)

# Operadores em PYTHON são os mesmos de JAVA <, <=, >, >=, ==, !=, ...

primValor = input('Digite um valor:\n')
segValor = input('Digite outro valor:\n')

cond = primValor<segValor

if cond:
    print(f'Condição é: {cond}')
else:
    print(False)


# IF COM AND
# A BARRA INVERTIDA DEFINE QUE POSSUI CONTINUAÇÃO NA LINHA ABAIXO
if (1 == 1 and 10 == 10) \
    or 5 == 'abcde':
    print(True)
else:
    print(False)

senha = input("Senha: ")

if senha != '1234':
    print('Senha Incorreta')

# Valida se a senha está nula - se o valor é falsy
if not senha:   
    print('Senha não pode estar em branco')