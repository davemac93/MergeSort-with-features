import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i = 0 #left_arr idx
        j = 0 #right_arr idx
        k = 0 #merged array idx
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def randomArray():
    arr = []
    k = int(input("Enter the lenght of the array: "))
    for i in range(k):
        x = random.randint(0, 10)
        arr.append(x)
    return arr

arr = randomArray()
n = len(arr)
print("Before:", arr)
st = time.time()
merge_sort(arr)
et = time.time()
print("After:", arr)
print('Execution time:', et - st, 'seconds')

