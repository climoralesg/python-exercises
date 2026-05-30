#40	Clasifica edades (niño, joven, adulto).
edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Edad no válida")
elif edad <= 12:
    print("Niño")
elif edad <= 17:
    print("Joven")
else:
    print("Adulto")