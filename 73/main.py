#73	Calcula el promedio de valores en un diccionario.

diccionario = {
    "valor1":1,
    "valor2":2,
    "valor3":3,
    "valor4":4,
    "valor5":5,
}

acc = 0.0
accNumbers = 0
for clave,valor in diccionario.items():
    parsedValor = float(valor)
    acc += valor
    accNumbers += 1


print(f"{(acc/accNumbers): .2f}")

promedio = sum(diccionario.values())/ len(diccionario)

print(f"{promedio:.2f}")
