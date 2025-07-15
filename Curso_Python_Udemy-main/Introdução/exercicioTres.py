"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

#Também poderia ser validade com num.isdigit()
try:
    num = int(input('Digite um número inteiro\n'))
    isEven = num%2 == 0
    print(f'É par: {isEven}')
except:
    print('Não número')

try:
    hora_int = int(input('Informe a hora\n'))
    if (hora_int < 0) or (hora_int > 23):
        print('Hora deve ser entre 0 e 23')
    elif (hora_int <= 11):
        print('Bom dia')
    elif (hora_int <= 17):
        print('Boa tarde')
    else:
        print('Boa noite')
except:
    print('Digite um valor int')

nome = input('Digite seu nome\n')
if nome:
    if len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande ')