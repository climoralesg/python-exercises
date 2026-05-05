#50	Pide números hasta que el usuario escriba “stop”.

while True :
    wordOrNumber = input("Ingresa una palabra y/o numero\n")
    
    if wordOrNumber.lower() == "stop" and wordOrNumber.lower().startswith("stop") :
        break
    else :
        if wordOrNumber.isdigit():

            number = int(wordOrNumber)
            print(f"El dato ingresado es el {number}\n")
        else:
            print("Ingrese un numero")