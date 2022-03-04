lista = [3,4,5,8,2,1]
def quicksort(array):
    
    if len(array)<2:
        return array
    else:
        pivo=array[0]
        menores=[i for i in array[1:] if i<=pivo]
        maiores = [i for i in array[1:]if i>pivo]
        return quicksort(menores) +[pivo] + quicksort(maiores)


print(quicksort(lista))