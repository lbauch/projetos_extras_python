"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

# Importa Sistema Operacional
import os

lista = []
s = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air\n')
while s != 's':
    if s =='i':
# Limpa o console
        dado = input('Oque deseja inserir?\n')
        lista.append(dado)
    elif s == 'a':
        if len(lista) == 0:
            print('Nada para apagar')
        else:
            try:
                dado = int(input('Qual índice deseja apagar?\n'))
                print(f'Valor excluído: {lista[dado]}')
                del lista[dado]
            except ValueError:
                print('Índice deve ser um nº inteiro')
            except IndexError:
                print('Índice não encontrado')
            except Exception:
                print('Erro desconhecido')
    elif s == 'l':
        if len(lista) == 0:
            print('Nada para listar')
        else:
            for i, valor in enumerate(lista):
                print(i, valor)
    elif s != 's':
        print('valor não reconhecido')
    s = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air\n')
    os.system('cls')

