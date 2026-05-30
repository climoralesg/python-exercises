#34	Verifica si un carácter es vocal o consonante.

letter = input("Ingresa una letra ")

vocals = [
    "a",
    "e",
    "i",
    "o",
    "u",
]

isVocal = letter in vocals

print(f"{isVocal}")

if isVocal:
    print("Es una vocal")
else:
    print("Es una consonante")
