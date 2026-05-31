#1
'''
Santa ha recibido una lista de regalos, pero algunos están defectuosos. Un regalo es defectuoso si su nombre contiene el carácter #.
Ayuda a Santa escribiendo una función que reciba una lista de nombres de regalos y devuelva una nueva lista que solo contenga los regalos sin defectos.

'''

gifts1 = ['car', 'doll#arm', 'ball', '#train']

def filterGifts(gifts : list):
    newFilters = []
    for i in range(0, len(gifts)):
        if '#' not in gifts[i]:
            newFilters.append(gifts[i])
    return newFilters


giftFiltered = filterGifts(gifts1)
print(f"{giftFiltered}")
