#While Else - Recurso exclusivo de Python

string = 'texto qualquer'

i=0
while i< len(string):
    print(string[i])
    i += 1
else:
    print('executou o else')
print('fora do while')

#não executa o while, então não executa o else
i=30
while i< len(string):
    print(string[i])
    i += 1
else:
    print('executou o else')
print('fora do while')