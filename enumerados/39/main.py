#39	Verifica si un usuario tiene acceso.

user = input("Ingrese su nombre")

validUsers =['claudio', 'juan']

if user in validUsers:
    print("El elemento se encuentra")
else:
    print("El elemento no se encuentra")