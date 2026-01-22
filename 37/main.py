#37	Determina la estación del año según el mes.

month = input("Ingresa un mes ")

match month :
    case "Diciembre"| "Enero"| "Febrero" :
        print("Estas en verano")
    case "Marzo" | "Abril" | "Mayo":
        print("Estás en otoño")
    case "Junio" | "Julio" | "Agosto":
        print("Estás en invierno")
    case "Septiembre" | "Octubre" | "Noviembre":
        print("Estás en primavera")


