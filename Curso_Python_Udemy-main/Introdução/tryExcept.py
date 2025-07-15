num_str = input('Calcular o dobro de um número. Digite o número:\n')

#Apenas introfução
try:
    print(f'o dobro de {num_str} é {float(num_str)*2:0.2f}')
except:
    print('Não foi digitado um número')
