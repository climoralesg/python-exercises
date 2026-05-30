#69	Busca un valor dentro de una lista.

lista = [1,2,"manzana",4,5,6]

indice = lista.index("manzana")

print(indice)

if "manzana" in lista:
    print("el valor se encuentra en la lista")

indice = lista.index("naranja")

print(indice)