from typing import List

def quick_sort(array: List) -> List:
    # if array is a single element array, return array
    if len(array) == 1:
        return array

    pivot = array[len(array)-1]
    head = array[0]
    head_position = 0
    pivot_position = len(array)-1
    
    while True:
        if head>pivot:
            new_head = array[pivot_position-1]
            array[pivot_position-1] = pivot
            array[pivot_position] = head

            # array has been sorted, now return result
            if len(array) == 2:
                return array
            else:
                
                # if there's no element between head and pivot.
                # This means the pivot is in the right spot and the subarrays on both sides of the pivot need to be sorted
                if head_position == pivot_position-1:
                    pivot_position = pivot_position-1
                   
                    # split the main array into two parts with the current pivot as the middle and sort those two parts recursively

                    # if there are elements before pivot
                    if array[:pivot_position] != []:
                        a = quick_sort(array[:pivot_position])
                        array[:pivot_position] = a

                    # if there are elements after pivot
                    if array[pivot_position+1:] != []:
                        b = quick_sort(array[pivot_position+1:])
                        array[pivot_position+1:] = b
                    return array
                        
                else:
                    array[head_position] = new_head
                    pivot_position = pivot_position-1
                    head = new_head  
        else:
            # return array(because it's sorted already)
            if len(array) == 2:
                return array

            # if there's no element between head and pivot.
            if head_position == pivot_position-1:

                # if there are elements before pivot
                    if array[:pivot_position] != []:
                        a = quick_sort(array[:pivot_position])
                        array[:pivot_position] = a
            
                    # if there are elements after pivot
                    if array[pivot_position+1:] != []:
                        b = quick_sort(array[pivot_position+1:])
                        array[pivot_position+1:] = b

                    return array
            
            else:
                head = array[head_position+1]
                head_position = head_position+1
    return array


print('result: ')
print(quick_sort([1000,2,70,200,8,1,3,0,7,2,10,50,6,200,7]))