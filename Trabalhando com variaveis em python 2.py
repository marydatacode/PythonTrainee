#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exemplo de variáveis em uma só linha
a,b,c = 'mercedes','prosh','ferrari'
print(a)
print(b)
print(c)


# In[3]:


# um valor para múltiplas variáveis
x=y=z='Estados Unidos'
print(x)
print(y)
print(z)


# In[5]:


# Unpack (descompactando) uma coleção de valores
paises=['Alemanha','Brasil','Estados Unidos']
x,y,z=paises
print(x)
print(y)
print(z)


# In[10]:


# Output variables: variaveis de saida
x='melhor que o Android'
print('o iPhone é'+ ' ' + x)


# In[11]:


# adicionando variaveis me python
x = 'o iPhone é '
y = 'melhor que o Android'
z = x + y
print(z)


# In[13]:


# adicionando variaveis para valores matematicos
x = 7
y = 3
print(x + y)


# In[20]:


# combinando string com integer
x = 'o valor do iPhone é'
y = str(1990)
print(x + y)


# In[19]:


# combinando string com integer com espaço
x = 'o valor do iPhone é'
y = str(1990)
print(x + ' ' + y)


# In[23]:


# variaveis globais
x = 'a profissão que mais cresce nesta decada'

def myfunc():
    print('data science é' + x)
myfunc ()


# In[ ]:





# In[ ]:




