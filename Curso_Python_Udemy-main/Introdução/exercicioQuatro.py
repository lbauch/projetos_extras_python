# Qual letra aparece mais vezes na frase?
frase = 'O Python é uma linguagem de programação multiparadigma'\
    'Python foi criado por Guido Van Rossum.'

fraseUpper = frase.upper()
maiorQtdCarac = 0
maiorQtdLetra = 0
maiorQtdLetraMai = 0
caracMaisComum = '' 
letraMaisComum = ''
letraMaisComumSemCase = ''

i = 0
while i < len(frase):
    contSemCase = fraseUpper.count(fraseUpper[i])
    cont = frase.count(frase[i])
    if cont > maiorQtdCarac:
        caracMaisComum = frase[i]
        maiorQtdCarac = cont
    
    if frase[i] != ' ' and cont > maiorQtdLetra:
            letraMaisComum = frase[i]
            maiorQtdLetra = cont
    
    print(frase[i], cont)

    if fraseUpper[i] != ' ' and cont > maiorQtdLetraMai:
         letraMaisComumSemCase = fraseUpper[i]
         maiorQtdLetraMai = contSemCase
    i += 1
print(f'letra mais comum: {letraMaisComum}, vezes: {maiorQtdLetra}')
print(f'carac mais comum: {caracMaisComum}, vezes: {maiorQtdCarac}')
print(f'carac mais comum: {letraMaisComumSemCase}, vezes: {maiorQtdLetraMai}')