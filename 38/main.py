#38	Calcula el impuesto según salario.
salario = float(input("Ingresa tu salario: "))

if salario <= 10000:
    impuesto = salario * 0.05
elif salario <= 20000:
    impuesto = salario * 0.10
elif salario <= 35000:
    impuesto = salario * 0.15
else:
    impuesto = salario * 0.20

print("El impuesto a pagar es:", impuesto)
print("Salario neto:", salario - impuesto)
