#66	Crea una lista y agrega elementos dinámicamente.

lista = [1,3,4,5,6]
print(lista)
lista.append(7)
lista.insert(1,"hola")
lista.extend(["nuevo","elemento"])

for i in range(0,len(lista)):
    print(f"{lista[i]}")