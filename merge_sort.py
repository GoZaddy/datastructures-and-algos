# each round has a list of lists whose size gets smaller as more of the original array gets sorted



def merge_sort(arr: [int]):
    print("Array to be sorted")
    print(arr)
    a = []
    b = []
    for i in arr:
        a.append([i])
    print("ROUND RESULT:")
    print(a)
    while (len(a) != len(arr)) or (isinstance(a[0], list)):
        for i in range(0, len(a), 2):
            if i == len(a)-1:
                b.append(a[i])
                break                
            if len(a[i]) == 1 and len(a[i+1]) == 1:
                if a[i][0] < a[i+1][0]:
                    b.append(a[i]+a[i+1])
                else:
                    b.append(a[i+1]+a[i])
        
            else:
                res = []
                a1 = a[i]
                c = a1[0]
                a2 = a[i+1]
                
                while len(a2) != 0 and len(a1) != 0:
                    ii = a2[0]
                    if c < ii:
                        res.append(c)
                        c = a1.pop(0)
                        if len(a1) == 0:
                            res = res + a2
                            a2 = []
                        else:
                            c = a1[0]
                    else:
                        res.append(ii)
                        a2.pop(0)
                        if len(a2) == 0:
                            res = res + a1
                            a1 = []
                b.append(res)
        if len(b[0]) == len(arr):
            a = b[0]
        else:
            a = b
            print("ROUND RESULT:")
            print(a)
            b = [] 
    print("SORTED ARRAY:")
    return a


print(merge_sort([1000,2,70,200,8,1,3,0,7,2,10,50,6,200,7]))  #SORTED ARRAY: [0, 1, 2, 2, 3, 6, 7, 7, 8, 10, 50, 70, 200, 200, 1000]