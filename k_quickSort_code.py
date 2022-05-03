#k_quickSort_code
def partition(a,s,e):
    pivot = a[s]
    count = 0 
    for i in range(s,e+1):
        if a[i]<pivot:
            count+=1
    pivot_place = s+count
    a[s],a[pivot_place] = a[pivot_place],a[s]
    i = s
    j = e
    while i<j:
        if a[i]<pivot:
            i+=1
        elif a[j]>pivot:
            j-=1
        else:
            a[i],a[j] == a[j],a[i]
            i+=1
            j-=1
    return pivot_place

def quickSort(a,s,e):
    if s>=e:
        return
    p = partition(a,s,e)
    quickSort(a,s,p-1)
    quickSort(a,p+1,e)
a = [9,7,1,2,8,4,5,9]
quickSort(a,0,len(a)-1)
print(a)