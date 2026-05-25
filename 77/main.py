#77	Cuenta la frecuencia de palabras en un texto.
from pprint import pprint
word = "con cuanta frecuencia hay una palabra palabra frecuencia con palabra"


arrayWord = word.split(' ')


print(arrayWord)

wordCount=[]

for i in range(0,len(arrayWord)):
    acc = 0
    wordCompared = arrayWord[i]
    for j in range(0,len(arrayWord)):
        if arrayWord[j] == wordCompared:
            acc+=1

    wordCount.append({
        "palabra": wordCompared,
        "count":acc
    })

pprint(wordCount,width=60)


