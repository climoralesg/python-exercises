#53	Cuenta cuántos números positivos y negativos se ingresan.

totalNumbers = int(input(f"Ingresa el numero total para validar"))
totalPos = 0 
totalNeg = 0
totalZero = 0
for i in range(1,totalNumbers+1):
    number = int(input(f"{i}. "))
    if number > 0:
        totalPos += 1

    if number < 0:
        totalNeg += 1

    if number == 0:
        totalZero += 1

print(f"Positivos: {totalPos}\nNegativos: {totalNeg}\nTotal en Cero : {totalZero}")