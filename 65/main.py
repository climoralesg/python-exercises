#65	Recorre una palabra mostrando índice y letra.
word = input("Ingresa una palabra\n")

for index,letter in enumerate(word):
    print(f"letra {letter}, indice: {index}")