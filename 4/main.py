#Pide dos números y muestra resta, multiplicación y división.
firtsNumber = input("Ingresa el primer numero\n")
secondNumber = input("Ingresa el segundo numero\n")

div = float(float(firtsNumber)/float(secondNumber))
mult = int(int(firtsNumber)*int(secondNumber))
rest = int(int(firtsNumber)-int(secondNumber))

print(f"La division es {div:.2f}\n")
print(f"La multiplicacion es {mult}\n")
print(f"La resta es {rest}\n")

print(f"El tipo de la variable es {type(firtsNumber)}")

