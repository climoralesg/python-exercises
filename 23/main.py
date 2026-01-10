#23	Verifica si una persona es mayor de edad.

age = int(input("Ingrese su edad "))
adultAge = 18

if age >= adultAge:
    print("Esta persona es mayor de edad")
elif age < adultAge:
    print("Esta persona es menor de edad")
