import time
import random
from array import *
def insertionSort(arr):
 
    for i in range(1, len(arr)):
 
        key = arr[i]
        
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def merge_sort_with_insertion_sort(arr, n):
        if len(arr) > 1:
            if len(arr) > n:
                left_arr = arr[:len(arr)//2]
                right_arr = arr[len(arr)//2:]
        
                #recursion
                merge_sort_with_insertion_sort(left_arr, n)
                merge_sort_with_insertion_sort(right_arr, n)

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
            else:
                insertionSort(arr)

           

def randomArray():
    arr = []
    k = int(input("Enter the lenght of the array: "))
    for i in range(k):
        x = random.randint(0, 100000)
        arr.append(x)
    return arr

arr = randomArray()
n = int(input("Enter the highest number for Insertion Sort else it will be soreted by Merge Sort: "))
print("Before:", arr)
st = time.time()
merge_sort_with_insertion_sort(arr, n)
et = time.time()
print("After:", arr)
print('Execution time:', et - st, 'seconds')
