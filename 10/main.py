#10	Intercambia los valores de dos variables sin perder datos.

firstValue = input("Ingrese el primer valor: ") 
secondValue = input("Ingrese el segundo valor: ")
print(f"El primer valor {firstValue}")
print(f"El segundo valor {secondValue}")
aux = firstValue
firstValue = secondValue
secondValue = aux
print(f"El primer valor {firstValue}")
print(f"El segundo valor {secondValue}")