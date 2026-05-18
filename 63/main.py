#63	Encuentra el mayor número de una lista.

list  = [1,2,5,1,5]

nList = len(list)

for i in range(nList) :
    swapped = False    
    for j in range(0,nList-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
            swapped = True
    if not swapped: break

print(f"{list[len(list)-1]}")
