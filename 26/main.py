#26	Evalúa una calificación y muestra aprobado o reprobado.
score = float(input("Ingresa una nota"))

minScore = 4.0

if score < minScore:
    print(f"No has calificado con la nota {score}")
else:
    print("Pasaste!")