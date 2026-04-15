#1. printing 1 to 10 numbers using while loop
i= 1                                 #created a variable for starting number
while i <= 10:                        #starting while loop , it will run as long as the value is 10
    print(i)                          #printing the current value of 'i'
    i = i +1                           # increase i value by loop

#2.printing the sum of N natural number
N = int(input("enter the number: "))  #input from the user
x = 0                                #initalizwe variable
sum = 0
while x <= N:                         # adding 1 to N
    sum = sum +x
    x = x + 1                         #increase the value of x by loop
print("The sum is: ",sum)             #printing result

#3. printing even numbers
N = int(input("enter the number:"))   #input from the user
i = 2                                 #initial the even number wid variable
while i <= N:                         # it will loop until N
    print(i)
    i = i + 2                         #increasing 2, value by each number

#4.counter timer
print("4.printing counter timer")
n = int(input("enter the countdown number:"))  #input from the user
while n >= 1:                                  #loop until the value is 1 ,
    print(n)
    n = n -1                                   #decreasing one value by one

# 5. reverse a num
num = int(input("enter number: "))  #getting the num from user - 8476
rev = 0                             #initialize the reverse to zero
while num > 0 :                     # loop runs as long as num is 0
    l_digit = num % 10              #the last digit (reminder is    8476=6 ,       847=7,       84= 4,       8=0
    rev = rev * 10 + l_digit       # storing digit value into rev   0*10+6=6,      6*10+7=67,   67*10+4=674, 674*10+8=6748
    num = num // 10                # removing the last digit of num 8476//10= 847, 847//10= 84 ,84//10=8,    0-lops ends
print(rev)                          #printing op

# 6. sum of numbers
num = int(input("enter a number: "))   #127
sum = 0                                #initialize sum to zero
while num > 0:                         #loop runs until 0
    last_digit = num % 10              #(reminder of num -     127%10=7 ,  12%10=2,   1%10=1
    sum = sum + last_digit             # adding l_digit to sum 0+7=7       7+2=9      9+1=10
    num = num // 10                    #quotient               127//10=12  12//10=1   1//10=0 -loop ends
print(sum)

#7. finding maximum element in iist using without using max()
# i/p=[11,7,23,5] and o/p= 23

num = [11,7,23,5]             #storing list value in variable
temp = num[0]                 #assume the first value is maxium num[0]=11
i = 1                         #initialize the counter ,                                         [list i = 1,2,3],here num[i]=7 ,
while i < len(num):           #loop will run as long as the i value is less than length of list 1<4, 2<4,3<4, 4<4=! false
    if num [i] > temp :       #chcek if i value is greater than temp                            ->i=[1]=7 temp=11 7>11 ,i=23 temp=11 23>11, i=5 temp=23 5>23,
        temp = num [i]        #storing the max value in temp                                    ->        temp= 11     ,temp=23          , temp=23
    i = i +1                  #iterate the i value for looping                                  -> i=1+1=2,i[2]=23    , i=2+1=3 i[3]=5    , i = 3+1 =4 loop will end
print("maxium:",temp)         # printing the result


# 8. Count even and odd numbers in a list
# Input: [1, 2, 3, 4, 5], Output: Even=2, Odd=3
num = [1,2,3,4,5]  #storing items in list variable
i = 0                         #initialize counter
even = 0                      #create a variable for storing a even count
odd = 0                       #create a variable for storing a odd count
while i<len(num):             #i=0,1,2,3,4 ,i=5-> 5<4 #loop will end                             loop will run as long as the i is less than of length of the list
    if num[i] % 2 == 0 :      #um[0]=1%2=1,num[1]=2%2=0,num[2]=3%2=1.num[3]=4%2=0,num[4]=5%2=1,  checking the item have the reminder 0 n
        even += 1             #even = 0    even = 1,    even =1,     even=2,      even =2        increasing the even count
    else:
        odd += 1              #odd=1,      odd = 1,     odd=2,       odd=2,       odd= 3         else the item will be count in odd
    i = i+1                   #i=0+1=1,    i=1+1=2,     i=2+1=3,     i=3+1=4,     i=4+1=5,      iterating loop
print("even count: ",even)    #printing result
print("odd count: ", odd)

#9.Reverse a list using while
# Input: [1, 2, 3, 4],Output: [4, 3, 2, 1] try with right index
# print(len(num)-1)            #left indexing
# print(-len(num))             #right indexing
# print (num[len(num)-1])      #left indexing
# print (num[-len(num)])       #right indexing
num = [1,2,3,4]
x = len(num)+1
y =[]
while x >= 0:
    y.append(num[x])
    x+=1
print(y)

#10.Remove duplicates manually using while loop
#Input:[1,2,2,3,1]

num=[1,2,2,3,1]                                 #storing items in list
unique = []                                     #create an empty temp list
i = 0                                           #intialize counter
while i < len(num):                             #loop will run as long as the i is less than length of list
    if num[i] not in unique:                     #check if current element is not already in unique lis
        unique.append(num[i])
    i += 1                                       #iterating item for loop
print("List after removing duplicates:", unique)

# Find the length of a tuple without using len()
# Input: (7, 8, 9, 10) Output: 4
num = (7,8,9,10)
x=0
count=0
while x < len(num):
     count+=1
     x=x+1
print(x)

# 11. Convert tuple to list manually using while
# Input: (5, 10, 15)
# Output: [5, 10, 15]

num = (5,10,15)         #storing values in variable
x=0                     #intialize index
y=[]                    #create empty list
while x < len(num):     #loop will run as long as the x value is less than of length of the variable 'num'
      y.append(num[x])  #adding value into empty list
      x=x+1             #iterating loop
print(y)                #printing statement


# 12.Sum all values in a dictionary
# Input: {"x": 10, "y": 20, "z": 30} ,Output: 60

a={"x":10,"y":20,"z":30}
b = list(a.values())
# print(b)
# print(len(b))
i= 0                         #intial index
summ=0
while i < len(b):
    summ = summ + b[i]
    i = i+1
print(summ)

#13.Count how many values are greater than a threshold ,
# Input: {"a": 5, "b": 10, "c": 15},threshold=8,Output: 2
a = {"a":5, "b": 10, "c": 15}
b= list(a.values())
# print(b)
threshold = int(input("enter a threshold value: "))
i = 0
count = 0
while i <len(b):
    if b[i]> threshold:
        count+=1
    i+=1
print("output:", count)


#14.Finding the second largest [8,10,7,12,9]
num=[8,10,17,12,9]
f_lar = sec_lar = num[0]
for n in num:
    if n>f_lar:
        sec_lar=f_lar
        f_lar=n
    elif n>sec_lar and n!=f_lar:
        sec_lar=n
print("14.second large:" , sec_lar)

#15.Remove All Occurrences of a Given Element ,Input: [1, 2, 3, 2, 4, 2], remove 2 Output: [1, 3, 4]
num=[1,2,3,2,4,2]
output=[]
remove=2
for n in num:
    if n != remove:
        output.append(n)
print("15." , output)

#16. Find Element Index Manually
#Input: (10, 20, 30, 40), find 30 Output: 2
num=(10,20,30,40)
find=30
for i in range(len(num)):
    if num[i]==find:
        print("16.index of value:",i)
        break

# 17. Check Whether a Number is Prime or Not
# Example:Input: 7 Output: Prime number
n=int(input("17.enter a value:"))
for i in range(2,n):
    if n%i==0:
        print("not prime number")
        break
else:
    print("prime number")

# #18. Prime Number Series
# # Example:Input: N = 10 Output: 2, 3, 5, 7
n=int(input("18.enter the value:"))
output=[]
for num in range(2,n+1):
    for i in range (2,num):
     if num % i==0:
        break
    else:
      output.append(num)
print(output)



# Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1
# Prompt the user to input the number of rows
row_num = int(input("Input number of rows: "))
# row_num=3
# Prompt the user to input the number of columns
col_num = int(input("Input number of columns: "))
# col_num=2

# Create a 2D list (a list of lists) filled with zeros using list comprehension
# The outer list will have 'row_num' elements and the inner lists will have 'col_num' elements
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
#col=0, , row=0,1,2

# Nested loop to populate the 2D list with multiplication results
for row in range(row_num):
    for col in range(col_num):
        # Set the value at position [row][col] in the 2D list to the product of 'row' and 'col'
        multi_list[row][col] = row * col

# Print the resulting 2D list containing the multiplication table
print(multi_list)


# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def example():
    try:
      x = 10
      y = 20
      print(x / y)
    except ZeroDivisionError:
        print("cant divide")
example()


























