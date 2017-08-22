# Python 3.5+

def quicksort(array):
    lt = []
    eq = []
    gt = []

    if len(array) > 1:
        pivot = array[0]

        for x in array:
        
            if x < pivot:
                lt.append(x)
                
            if x == pivot:
                eq.append(x)
                
            if x > pivot:
                gt.append(x)

        return [*quicksort(lt), *eq, *quicksort(gt)]

    return array

print(quicksort([123, 14255, 124, 1435, 124213, 11, 1, 0, 149, 903, 99, 310, 103, 102]))
