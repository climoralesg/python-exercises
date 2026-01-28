#41	Determina tipo de triángulo.
a = float(input("Ingrese el primer lado: "))
b = float(input("Ingrese el segundo lado: "))
c = float(input("Ingrese el tercer lado: "))

if a == b == c:
    print("Triángulo equilátero")
elif a == b or a == c or b == c:
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")