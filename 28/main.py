#28	Verifica si una contraseña es correcta.

password = input("Ingrese su contraseña: ")

passwordVer = "password"

resultView = (password == passwordVer)

print(f"{resultView}")

if resultView:
    print("Contaseña aceptada")
else:
    print("Contraseña incorrecta")

