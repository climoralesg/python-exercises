#57	Implementa un menú que se repite hasta salir.

while True:
    print("Ingrese una opcion del menu")
    print("1.Continuar")
    print("2.Salir\n")
    menu = int(input())
    match menu:
        case 1:
            print("Elegiste Repetir")
        case 2:
            break
        case _:
            print("Comando no reconocido")