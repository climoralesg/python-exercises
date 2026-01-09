#19	Pide al usuario su ingreso mensual y sus gastos mensuales, y calcula cuánto dinero ahorra en un mes.

moneyIncomeMonthly = float(input("Ingresa cuanto dinero entra en el mes: "))
moneyExpensesMonthly = float(input("Ingresa cuanto fueron tus gastos al mes: "))

result = moneyIncomeMonthly - moneyExpensesMonthly

print(f"El resultado final es {result:.2f}")