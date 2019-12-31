import random

def is_sorted(array):
        heap = 0
        for item in array:
            if item < heap:
                return False
            heap = item
        return True

iterations = 0

def bogo_sort(array):
    global iterations
    sorted = False
    while sorted is False:
        iterations += 1
        random.shuffle(array)
        sorted = is_sorted(array)
    return array

def bogo_bogo_sort(array):
    sorted_array = []
    for item in array:
        sorted_array.append(item)
        sorted_array = bogo_sort(sorted_array)
    return sorted_array
    
            

array = random.sample(range(1,10), 9)
print(f'Unsorted:\t{array}')
print(f'Sorted: \t{bogo_bogo_sort(array)}')
print(f'Iterations:\t{iterations}')

            
        

