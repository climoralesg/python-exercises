#44	Determina turno según hora.

time = input("Ingrese su horario de entrada\n")
turn = int(input("1.AM\n2.PM\n"))

match turn:
    case 1:
        print(f"Entonces entraras en la mañana a las {time}")
    case 2:
        print(f"Entonces entraras en la tarde a las {time}")
    case _:
        print("Horario no reconocido")
