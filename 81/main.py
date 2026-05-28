#81	Crea una lista vacía y permite al usuario agregar 5 números.
list = []

for i in range(5):
    list.append (int(input(f"Ingrese el valor de la posicion {i}: ")))

print(list)

