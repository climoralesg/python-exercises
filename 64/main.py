#64	Cuenta números pares en una lista.
list = [2,4,5,6,7,8,0,9,10]
pairAcc = 0

for i in range(0, len(list)):
    print(f"{list[i]}")
    if list[i] % 2 == 0 :
        pairAcc += 1

print(f"El numero de pares es {pairAcc}")