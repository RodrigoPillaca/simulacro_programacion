def ord_burbuja(array):
    longitud = len(array)
    
    for i in range(longitud):
        for j in range(longitud - 1 - i):
            if array[j] > array[j+1]:
                temporal = array[j+1]
                array[j+1] = array[j]
                array[j] = temporal
    return array
            
array = [8, 3, 1, 19, 14]
print(array)
print(ord_burbuja(array))