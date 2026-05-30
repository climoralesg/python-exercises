#33	Simula un semáforo según el color ingresado.

color = input("Ingrese un color: ")

colors= { 
    "rojo":"Parar",
    "amarillo": "alerta",
    "verde": "Siga"
}

result =  colors.get(color.lower(),"no se encuentra accion")

print(f"La accion es {result}")


