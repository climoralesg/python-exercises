#27	Convierte una nota numérica en letra.

score = input("Ingresa tu nota: ")

numbers = {
    1:"Uno",
    2:"Dos",
    3:"Tres",
    4:"Cuatro",
    5:"Cinco",
    6:"Seis",
    7:"Siete",
    8:"Ocho",
    9:"Nueve"
}

firstNumber = numbers.get(int(score[0]),"No se encuentra")
secondNumber = numbers.get(int(score[1]), "No se encuentra")

print(f"Nota final {firstNumber} , {secondNumber}")

