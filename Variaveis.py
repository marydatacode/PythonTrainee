# Exemplo de variáveis em uma só linha
a,b,c = 'mercedes','prosh','ferrari'
print(a)
print(b)
print(c)

# um valor para múltiplas variáveis
x=y=z='Estados Unidos'
print(x)
print(y)
print(z)

# Unpack (descompactando) uma coleção de valores
paises=['Alemanha','Brasil','Estados Unidos']
x,y,z=paises
print(x)
print(y)
print(z)

# Output variables: variaveis de saida
x='melhor que o Android'
print('o iPhone é'+ ' ' + x)

# adicionando variaveis me python
x = 'o iPhone é '
y = 'melhor que o Android'
z = x + y
print(z)

# adicionando variaveis para valores matematicos
x = 7
y = 3
print(x + y)

# combinando string com integer
x = 'o valor do iPhone é'
y = str(1990)
print(x + y)

# combinando string com integer com espaço
x = 'o valor do iPhone é'
y = str(1990)
print(x + ' ' + y)

# variaveis globais
x = 'a profissão que mais cresce nesta decada'

def myfunc():
    print('data science é' + x)
myfunc ()




