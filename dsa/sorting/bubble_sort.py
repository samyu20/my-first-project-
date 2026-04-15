'''Bubble Sort'''
def bubble_sort(ml):   #ml=my list
    n=len(ml)
    for i in range(n-1):
        for j in range (n-i-1):
            if ml[j]>ml[j+1]:
                ml[j],ml[j+1]=ml[j+1],ml[j]
    return ml
ml=[8,4,5,9,2]
print(bubble_sort(ml))

def bubble_sort(list1):
    n=len(list1)
    for i in range(n-1):                                         #7-1=6, [0,1,2,3,4,5]
        swapped= False                                           #checking if any swap occur
        for j in range(n-i-1):                                   #7-0-1=6 [0,1,2,3,4,5]
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
                swapped =True
        if not swapped:                                          #if no swap occur loop will stop
            break
    return list1
list1=[13,25,56,19,8,98,2]
print(bubble_sort(list1))