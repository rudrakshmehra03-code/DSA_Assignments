import random
import time
import sys
sys.setrecursionlimit(10000)

ran_arr = random.choices(range(1000), k=1000)
sorted_arr = [x for x in range(1000)]
reverse_arr = [x for x in range(1000, 0, -1)]


inp_1 = int(input("Enter the dataset you want to sort(random=1, ascended=2, descended=3): "))
inp_2 = int(input("Enter the algorithm you want to use(insertion=1, quick=2, merge=3): "))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        # print("key", key, "j", j)
        # print(arr)
    return arr

#########################################
def partition(arr, low, high):
    pivot = arr[high]
    j = low - 1
    for i in range(low, high):
        if arr[i] < pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[j + 1], arr[high] = arr[high], arr[j + 1]
    return j + 1

def quick_sort(arr, low, high):
    if low < high:
        q = partition(arr, low, high)
        quick_sort(arr, low, q - 1)
        quick_sort(arr, q + 1, high)
    return arr


#######################################
def merge(ar, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0] * n1
    right = [0] * n2
    for i in range(n1):
        left[i] = ar[p + i]
    for j in range(n2):
        right[j] = ar[q + j + 1]

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            ar[k] = left[i]
            i += 1
        else:
            ar[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        ar[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        ar[k] = right[j]
        j += 1
        k += 1


def merge_sort(ar, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(ar, p, q)
        merge_sort(ar, q + 1, r)
        merge(ar, p, q, r)
    return ar

##########################################

if inp_1 == 1:
    print("Random array", ran_arr)
    if inp_2 == 1:
        print(insertion_sort(ran_arr))
    elif inp_2 == 2:
        print(quick_sort(ran_arr, 0, len(ran_arr) - 1))
    elif inp_2 == 3:
        print(merge_sort(ran_arr, 0, len(ran_arr) - 1))

elif inp_1 == 2:
    print("ascended arr", sorted_arr)
    if inp_2 == 1:

        print(insertion_sort(sorted_arr))
    elif inp_2 == 2:
        print(quick_sort(sorted_arr, 0, len(sorted_arr) - 1))
    elif inp_2 == 3:
        print(merge_sort(sorted_arr, 0, len(sorted_arr) - 1))
elif inp_1 == 3:
    print("descended arr", reverse_arr)
    if inp_2 == 1:
        print(insertion_sort(reverse_arr))
    elif inp_2 == 2:
        print(quick_sort(reverse_arr, 0, len(reverse_arr) - 1))
    elif inp_2 == 3:
        print(merge_sort(reverse_arr, 0, len(reverse_arr) - 1))
else:
    print("Please enter a valid input, please try again.")

print("Time Taken", time.process_time(), "ms")