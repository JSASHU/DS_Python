arr = [1,10,5,6,1,0,23,50]

def partition(arr, start, end):
    pivot = arr[end]
    pindex = start
    
    for index in range(start, end):

        if(arr[index] <= pivot):
            temp = arr[pindex]
            arr[pindex] = arr[index]
            arr[index] = temp
            pindex = pindex + 1
    new_temp = arr[pindex]
    arr[pindex] = arr[end]
    arr[end] = new_temp
    
    return pindex

def quickSort(arr, start , end):

    if(start < end):
        pindex = partition(arr, start, end)
        quickSort(arr, start, pindex-1)
        quickSort(arr, pindex+1, end)

quickSort(arr, 0, len(arr)-1)

print arr