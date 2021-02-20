def bubble_sort(array:list) -> list:
    i = 0
    while is_sorted(array) == False:
        if array[i] > array[i+1]:
            onePlusI = array[i+1]
            arrayI = array[i]
            array[i] = onePlusI
            array[i+1] = arrayI

        if i == len(array)-2:
            i = 0
            print(array)
        else:
            i=i+1
        

    return array


def is_sorted(array):
    for i,_ in enumerate(array):
        if i == len(array)-1:
            continue
        else:
            if array[i] > array[i+1]:
                return False
    return True

print(bubble_sort([21,4,1,3,9,20,25,6,21,14]))