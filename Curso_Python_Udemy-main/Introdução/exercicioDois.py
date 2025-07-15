nome = input('Digite seu nome\n')
idade = input('Digite sua idade\n')

if nome and idade :
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if " " in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')
    print(f'seu nome contém {len(nome)} caracteres')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Todos os campos são obrigatórios')