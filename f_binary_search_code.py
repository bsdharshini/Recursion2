#f_binary_search_code.py
def binary_search(arr,n,s,e):
    if s>e:
        return -1
    mid = (s+e)//2
    if arr[mid]>n:
        return binary_search(arr,n,s,mid-1)
    elif arr[mid]<n:
        return binary_search(arr,n,mid+1,e)
    else:
        return mid
arr = list(int(i) for i in input().strip().split())
n = int(input())
print(binary_search(arr,n,0,len(arr)-1))
    


"""
# need to work 
def binary_search(arr,n):
    l = len(arr)
    if l == 0:
        return -1
    mid = l // 2
    if arr[mid] == n:
        return mid
    elif arr[mid]>n:
        return binary_search(arr[0:mid],n)
    else:
        return binary_search(arr[mid+1:l],n)
print(binary_search([1,2,3,4,5,6,7,8],7))"""