#72	Busca una clave en un diccionario.

diccionario = {
    'Claudio':30,
    'Victor':38,
    'Alvaro': 27
}

print(f"{diccionario['Claudio']}")

print(diccionario)

valor = diccionario.get("Victor")

print(f"Valor encontrado {valor}")

valor= diccionario.get("Pedrito")

print(f"Valor no encontrado {valor}")

valor= diccionario.get("Pedrito","Por defecto")

print(f"Valor no encontrado en default {valor}")