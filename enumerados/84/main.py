#84	Calcula el promedio de una lista.

def calProm(originalList: list[int]) -> float:
    acc = 0.0     
    numberActive = 0
    for i in range(0,len(originalList)):
        if type(originalList[i]) == int or type(originalList[i]) == float:
            acc+= float(originalList[i])
            numberActive+=1
    if numberActive == 0:
        return 0.0
    return acc / numberActive
def main():
    list = [2,2,"hola",3]
    result = calProm(list)
    print(f"{result:.2f}")

if __name__=="__main__":
    main()