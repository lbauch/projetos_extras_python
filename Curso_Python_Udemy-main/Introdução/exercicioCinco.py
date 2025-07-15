"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra = 'abcde'
letrasAcertadas = ''
palavraSenha = ''
tentativas = 0

while palavraSenha != palavra:
    letraInformada = input('Digite uma letra\n')
    if len(letraInformada) != 1:
        print('Somente aceitas letras únicas')
    elif letraInformada in letrasAcertadas:
        print('Esta letra Já foi digitada')
    elif letraInformada in palavra:
        letrasAcertadas += letraInformada
        palavraSenha = ''
        for letra in palavra:
            if letra in letrasAcertadas:
                palavraSenha += letra
            else:
                palavraSenha += '*'
        print(palavraSenha)
    tentativas += 1
else:
    print(f'Parabéns! Você descobriu a palavra: {palavra} em {tentativas} tentativas')
