
word = "1234567987654321234567876543212345"
nums = ['0','2','4','6','8']

numsCount = 0

for character in word:
    if character in nums:
        numsCount += 1
        
print(numsCount)

mytuple = ('gol','saveiro','fusca')

for x in mytuple:
    print(x)

for x in range(9):
    print(x)

for x in range(0,22,2):
    print(x)

pares = [0,2,4,6,8]
for x in pares:
        print(x)

frutas = ['uva','banana','limão']
for x in frutas:
    print(x)

for x in 'python':
    print(x)

paises = ['alemanha','australia','estados unidos','japao']
for x in paises:
    print(x)
    if x == 'estados unidos':
        break

linguagens = ['cobol','pythoon','c++']
for x in linguagens:
    if x == 'python':
        continue
    print(x)

for x in range(7):
    print(x)
else:
    print('concluido')

for x in range(10):
    if x == 5: break
    print(x)
else:
    print('concluido')

# Nested Loops

cores = ['vermelho','azul','verde']
carros = ['tiguan','audi','mercedes']

for x in cores: 
    for y in carros:
        print(x,y)


