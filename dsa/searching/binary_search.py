'''  BINARY SEARCH
Array must be sorted ,Compare with target:
Equal → return index
Target greater → search right half
Target smaller → search left half'''

def binary_search(arr,target):
    low=0
    high=len(arr)-1            #high=7
    while low <= high:
        mid = (low+high) // 2      #3, 5 ,6+7
        if arr[mid] == target:
            return mid             #target found
        elif arr[mid] < target:    # right search 14 < 22,22<27
            low = mid +1           # 3+1=4, [18]        ,5+1=6
        else :
            high = mid -1          #left search
arr=[3, 7, 10, 14, 18, 22, 27, 31]  #list must be sorted
target = 27
n=binary_search(arr, target)
if n is not None:
    print(n)
else:
    print("value is not found")









