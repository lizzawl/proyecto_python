
lista = [15,"nombre",3.1415,True]

print(lista[3])

usuario = ["usernameTest1","pass123","correo@correo.com"]

numeros = [10,50,100,255,500]

numeros.append(1000)
print(numeros)

extra = [75,350,999]
numeros.extend(extra)
print(numeros)

numeros.insert(6,5000)
print(numeros)

numeros.remove(50)
print(numeros)

numeros.pop()
print(numeros)
numeros.pop(3)
print(numeros)

numeros.reverse()
print(numeros)

numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)