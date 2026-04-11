# def bubble_sort(ml):   #ml=my list
#     n=len(ml)
#     for i in range(n-1):
#         for j in range (n-i-1):
#             if ml[j]>ml[j+1]:
#                 ml[j],ml[j+1]=ml[j+1],ml[j]
#     return ml
# ml=[8,4,5,9,2]
# print(bubble_sort(ml))

'''Bubble Sort'''

# def bubble_sort(list1):
#     n=len(list1)
#     for i in range(n-1):                                         #7-1=6, [0,1,2,3,4,5]
#         swapped= False                                           #checking if any swap occur
#         for j in range(n-i-1):                                   #7-0-1=6 [0,1,2,3,4,5]
#             if list1[j] > list1[j+1]:
#                 list1[j],list1[j+1] = list1[j+1],list1[j]
#                 swapped =True
#         if not swapped:                                          #if no swap occur loop will stop
#             break
#     return list1
# list1=[13,25,56,19,8,98,2]
# print(bubble_sort(list1))

# def selection_sort(arr):
#     n = len(arr)                          #n=8
#     for i in range(n - 1):                #8-1 = 7 [0,1,2,3,4,5,6]
#         min_index = i                     #i=0,                                           ,i=1
#         for j in range(i + 1, n):         #j=(1,7)=[1,2,3,4,5,6]                          ,j=(2,7)=2,3,4,5,6
#             if arr[j] < arr[min_index]:   #1- 34 < 64 ,2- 25 < 34, 3- 5< 25,4- 22 < 5     ,2-> 34<64, 3->25<34,4->22<25,5->11<22,6-> 90<11
#                 min_index = j             #j=1,          j=2,       j=,3                  ,j=2      ,j=3      ,j=4     ,j=5
#         min_value = arr.pop(min_index)    #j=4,in.v=3 -> m.v= pop.3[64,34,25,22,11,90,94]  ,j=5 , m.v=pop(5)  [5,64,34,25,22,90,94]
#         arr.insert(i, min_value)          #i=(0,3)-> [5,64,34,25,22,11,90,94]              ,insert(1,5)   [5,11,64,34,25,22,90,94]
#     return arr
# # usage
# mylist = [64, 34, 25, 5, 22, 11, 90,94]
# sorted_list = selection_sort(mylist)
# print(sorted_list)


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

















