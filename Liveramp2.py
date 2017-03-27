# coding=utf-8
def find_left_of_arr(arr, length):
    for i in range(1,length):
        if arr[i]<arr[i-1]:
            break
    return i-1

def find_right_of_arr(arr,length):
    for i in range(length-2,-1,-1):
        if arr[i] > arr[i+1]:
            return i+1
    return 0

def shrinkleft(arr,min,max,findleft):
    for i in range(findleft,-1,-1):
        if arr[i]<=arr[min]:
            break
    max2 = i+1 if arr[i+1]>arr[max] else max
    return i+1, max2

def shrinkright(arr,min,max,findright,length):
    for i in range(findright,length):
        if arr[i]>=arr[max]:
            break
    min2 = i-1 if arr[i-1]<arr[min] else min
    return i-1, min2

def findsequence(arr,length):
    findleft = find_left_of_arr(arr,length)
    print findleft
    if findleft>=length-2:
        return 0
    findright = find_right_of_arr(arr,length)
    print findright
    min,max = findright,findleft
    for i in range(findleft+1,findright):
        if arr[i]<arr[min]:
            min = i
        if arr[i]>arr[max]:
            max = i


    finalleftindex,max2 = shrinkleft(arr,min,max,findleft)
    finalrightindex,min2 = shrinkright(arr,min,max,findright,length)
    '''while(max != max2 or min != min2):
        max, min = max2, min2
        finalleftindex, max2 = shrinkleft(arr, min, max, findleft)
        finalrightindex, min2 = shrinkright(arr, min, max, findright, length)'''

    return (finalrightindex-finalleftindex)

array = [1,2,6,0,0,18,19]
length = len(array)
print(findsequence(array,length))