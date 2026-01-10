#25	Compara tres números y muestra el mayor.

firstNumber = int(input("Ingresa el primer numero: ")) 
secondNumber = int(input("Ingresa el segundo numero: "))
thirdNumber = int(input("Ingresa el tercer numero: "))

if firstNumber > secondNumber and firstNumber > thirdNumber :
    print("El primer numero es mayor")
elif secondNumber > firstNumber and secondNumber > thirdNumber :
    print("El segundo numero es mayor")
elif(thirdNumber > firstNumber and thirdNumber > firstNumber) :
    print("El tercer numero es mayor")

resultMax = max(firstNumber, secondNumber, thirdNumber)
print(resultMax)