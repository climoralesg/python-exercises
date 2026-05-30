#71	Crea un diccionario con nombres y edades.

diccionario = {
    'Claudio':30,
    'Victor':38
}

print(f"{diccionario['Claudio']}")

print(diccionario)

for clave,valor in diccionario.items():
    print(f"Item {clave} su valor {valor}")