#52	Genera la serie Fibonacci hasta N términos.

serialNumber = int(input("Ingresa el valor de la serie\n"))

accNumber = 0

for i in range(1, serialNumber+1):
    tempValue = accNumber
    accNumber += i
    print(f"{tempValue} + {i} = {accNumber}")
    



