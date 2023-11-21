#!/usr/bin/env python
# coding: utf-8

# In[3]:


word = "1234567987654321234567876543212345"
nums = ['0','2','4','6','8']

numsCount = 0

for character in word:
    if character in nums:
        numsCount += 1
        
print(numsCount)


# In[4]:


mytuple = ('gol','saveiro','fusca')

for x in mytuple:
    print(x)


# In[5]:


for x in range(9):
    print(x)


# In[8]:


for x in range(0,22,2):
    print(x)


# In[11]:


pares = [0,2,4,6,8]
for x in pares:
        print(x)


# In[12]:


frutas = ['uva','banana','limão']
for x in frutas:
    print(x)


# In[20]:


for x in 'python':
    print(x)


# In[22]:


paises = ['alemanha','australia','estados unidos','japao']
for x in paises:
    print(x)
    if x == 'estados unidos':
        break


# In[25]:


linguagens = ['cobol','pythoon','c++']
for x in linguagens:
    if x == 'python':
        continue
    print(x)


# In[27]:


for x in range(7):
    print(x)
else:
    print('concluido')


# In[28]:


for x in range(10):
    if x == 5: break
    print(x)
else:
    print('concluido')


# In[29]:


# Nested Loops

cores = ['vermelho','azul','verde']
carros = ['tiguan','audi','mercedes']

for x in cores: 
    for y in carros:
        print(x,y)


# In[ ]:




