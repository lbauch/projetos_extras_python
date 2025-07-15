# Operadores como +=, -=, *=, %=, **= significam o mesmo que em java
# exemplo: contador += 1 significa contador = contador + 1
contador = 0
while contador <= 9:
    contador += 1
    print(contador)
    

# Para strings: 
# cont = 10
# cont *= '2' - imprime 2222222222

# CONDIÇÃO WHILE BREAK
while True:
    nome = input('Digite seu nome\n')
    print(f'seu nome é {nome}')
    
    if nome == 'sair':
        break

# CONDIÇÃO WHILE CONTINUE
contador = 0
while contador <= 9:
    contador += 1

    if  contador == 5 or contador == 6 or contador == 7:
        print('Parou')
        continue

    print(contador)