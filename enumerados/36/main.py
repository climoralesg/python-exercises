#36	Valida que un texto no esté vacío.

text = input("Ingresa un texto ")

textSplit = text.strip()

if not textSplit:
    print("La cadena esta vacia")
else:
    print("La cadena no esta vacia")