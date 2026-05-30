#43	Verifica si una letra es mayúscula.

letter = input("Ingresa una letra\n")[0]

if letter.isupper() :
    print(f"La letra {letter} es mayuscula")
else :
    print(f"La letra {letter} es minuscula")

