#9	Calcula el promedio de tres calificaciones.

firstQual = float(input("Ingrese la primera nota"))
secondQual= float(input("Ingrese la segunda nota"))
thirdQual = float(input("Ingrese la tercer nota"))

result = float((firstQual + secondQual + thirdQual)/3 )

print(f"El promedio de notas es {result:.2f}")