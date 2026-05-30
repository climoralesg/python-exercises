#47	Imprime los números pares del 1 al 100.

finalNumber = 100
initial = 1

for i in range(1,101):
    if i % 2 == 0:
        print(f"{i}")



while initial <= finalNumber:
    if initial % 2 == 0:
        print(f"{initial}")
    initial+=1