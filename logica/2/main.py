'''
La fábrica de Santa ha empezado a recibir la lista de producción de juguetes.
Cada línea indica qué juguete hay que fabricar y cuántas unidades.

Los elfos, como siempre, han metido la pata: han apuntado algunos juguetes con cantidades que no tienen sentido.

Tienes una lista de objetos con esta forma:

toy: el nombre del juguete (string)
quantity: cuántas unidades hay que fabricar (number)
Tu tarea es escribir una función que reciba esta lista y devuelva un array de strings con:

Cada juguete repetido tantas veces como indique quantity
En el mismo orden en el que aparecen en la lista original
Ignorando los juguetes con cantidades no válidas (menores o iguales a 0, o que no sean número)
'''


def manufactureGift( production : list):
    filterQuantityOK = list(filter(lambda x: x["quantity"] > 0 ,production))
    accProductsFinal = []
    readyProducts = []
    for i in range(0,len(filterQuantityOK)):

        if filterQuantityOK[i]["toy"] not in readyProducts:
            filterFound = list(filter(lambda x : x["toy"] == filterQuantityOK[i]["toy"] and x["quantity"] > 0, production))
            totalQuantity = 0
            for j in range(0,len(filterFound)):
                totalQuantity += filterFound[j]["quantity"]
            accProductsFinal.append({"toy":filterQuantityOK[i]["toy"],"quantity":totalQuantity})
            readyProducts.append(filterFound[0]["toy"])
    return accProductsFinal


production1 = [
    { "toy": 'ball',"quantity": -2 },
    { "toy": 'car', "quantity": 3 },
    { "toy": 'doll',"quantity": 1 },
    { "toy": 'ball',"quantity": 2 },
    { "toy": 'ball',"quantity": 2 }
]
production2 = [
  { "toy": 'train', "quantity": 0 }, # no se fabrica
  { "toy": 'bear', "quantity": -2 }, # tampoco
  { "toy": 'puzzle', "quantity": 1 }
]


print(production1)
result1 = manufactureGift(production1)
print(result1)







