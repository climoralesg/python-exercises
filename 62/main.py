#62	Suma los elementos de una lista.

list = [1,2,"hola",2,"a"]

acc = 0
for i in range(0,len(list)):
    if isinstance(list[i],int):
      acc+=list[i]  
    else:
        print(f"'{list[i]}' no es un numero")

print(f"El resultado final acumulado es: {acc}")