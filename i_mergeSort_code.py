#i_mergeSort_code.py

# create two fn 
# 1 fn for merge
# 1 fn for divide
# mergeSort can'tbe done without copying or slicing the list
def merge(arr,a,b):
    i,j,k = 0,0,0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            arr[k] = a[i]
            i+=1
            k+=1
        else:
            arr[k] = b[j]
            j+=1
            k+=1
    while i<len(a):
        arr[k]=a[i]
        i+=1
        k+=1
    while j<len(b):
        arr[k]=b[j]
        j+=1
        k+=1
def divide(arr):
    l = len(arr)
    if l == 0 or l ==1:
        return arr
    mid = l//2
    a = arr[0:mid]
    b = arr[mid:l]
    divide(a)
    divide(b)
    merge(arr,a,b)
a = [3,4,1,7,2,0,7]
divide(a)
print(a)