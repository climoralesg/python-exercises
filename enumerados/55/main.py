#55	Cuenta cuántas vocales tiene una palabra.

vocals =['a','e','i','o','u']

word = input("Ingrese una palabra")

accVocals = 0
for i in range(0,(len(word)-1)):
    if word[i] in vocals:
        accVocals+=0
    
print(f"El numero total de vocales es ")