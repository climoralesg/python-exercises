'''Los elfos han encontrado el código cifrado que protege la puerta del taller de Santa 🔐. El PIN tiene 4 dígitos, y está escondido dentro de bloques como estos:

[1++][2-][3+][<]
Escribe una función que descifre el PIN a partir del código.

El código está formado por bloques entre corchetes [...] y cada bloque genera un dígito del PIN.

Un bloque normal tiene la forma [nOP...], donde n es un número (0-9) y después puede haber una lista de operaciones (opcionales).

Las operaciones se aplican en orden al número y son:

+ suma 1
- resta 1
El resultado siempre es un dígito (aritmética mod 10), por ejemplo 9 + 1 → 0 y 0 - 1 → 9.

También existe el bloque especial [<], que repite el dígito del bloque anterior.

Si al final hay menos de 4 dígitos, se debe devolver null.

Ejemplos
decodeSantaPin('[1++][2-][3+][<]')
// "3144"

decodeSantaPin('[9+][0-][4][<]')
// "0944"

decodeSantaPin('[1+][2-]')
// null (solo 2 dígitos)'''

import re
def decodeSantaPin(code: str) -> str: 
  
  codeText = re.findall(r"\[(.*?)\]", code)

  password = ""

  for i in range(0,len(codeText)):
    #print(f"{codeText[i]}\n")
    
    accNumber = 0
    backNumber = 0
    if i > 0: 
      backNumber = codeText[i-1][0] 
    
    for j in range(0,len(codeText[i])):
      if j == 0 :
        if codeText[i][j] == '<':
          accNumber = backNumber
        else :  
          accNumber = int(codeText[i][j])
      else:   
        if codeText[i][j] == '+' :
          accNumber += 1

        if codeText[i][j] == '-' :
          accNumber -= 1
    password = password + str(accNumber)      

  return password

code = decodeSantaPin ("[1++][2-][3+][<]")

print(f"{code}")