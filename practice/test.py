#1.Write a Python function to find the first duplicate element in a sequence of numbers.
def first_duplicate(num):
    duplicates= set()
    for x in num:
        if x in duplicates:
            return x
        duplicates.add(x)
    return "no duplicate found"
print(first_duplicate([2,4,6,7,3,5,6,4,8,6]))

#.2 Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'.Ensure that each character is used only once.
import random
char_list=['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))

#Write a Python program that removes and prints every third number from a list of numbers until the list is empty.
def remove_3variable(data):
    index=0
    while data:
        index=(index+2)%len(data)
        removed=data.pop(index)
        print(removed)
num =[1,2,3,4,5,6,7,8,9,10]
remove_3variable(num)

# Fibonacci logic
def fibonacci_logic(n):
    a=0
    b=1
    for _ in range(n):
        print(a)
        next_num=a+b
        a=b
        b= next_num
num=int(input("enter your value: "))
if num <=0:
    print("please enter a positive num")
else:
    fibonacci_logic(num)

#Reverse a string without slicing
def reverse_string(n):
    reverse=""
    for char in n:
        reverse=char+reverse
    return reverse
user =input("enter a string: ")
print(reverse_string(user))

#Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
# between 1500 and 2700 (both included).
def finding_divisible():
    result=[]
    for i in range(1500,2701):
        if (i%7==0) and (i%5==0):
            result.append(str(i))
    return ','.join(result)
print(finding_divisible())

# Write a Python program to list numbers between 1000 and 3000 that are divisible by 7 but not by 5.
def is_divisible():
    result=[]
    for x in range(1000,3001):
        if (x%7==0) and (x%5!=0):
            result.append(str(x))
    return ",".join(result)

print(is_divisible())

#Write a Python program to count how many numbers between 1500 and 2700 are divisible by 7 and also multiples of 5.
def count():
    result=0
    for i in range(1500,2701):
        if (i%7==0) and (i%5==0):
            result=result+1
    return result
print(count())

#Write a Python program to compute the sum of numbers between 1500 and 2700 that are divisible by 7 and multiples of 5.
def count():
    result=0
    for i in range(1500,2701):
        if (i%7==0) and (i%5==0):
            result+=i
    return result
print(count())

#Write a Python program to convert temperatures to and from Celsius and Fahrenheit. , formula -> C = (5/9) * (F - 32)
def convert_temprature():
    choice=input("Enter 'C' to convert cel to fahren or 'F' tp convert faren to cel: ")

    if choice== 'C' or 'c':
        c= float(input("enter a temperature in celsius: "))
        f=(9/5)*(c+32)
        print("Fahrenheit:",f)


    elif choice=='F' or 'f':
        f=float(input("Enter a temperature in fahernheit: "))
        c=(5/9)*(f-32)
        print("Celsius:",c)

    else:
        print("Invalid input")
convert_temprature()

#Write a Python program to guess a number between 1 and 9.
import random
def guess_num():
    target=random.randint(1,9)

    while True:
        guess = int(input("guess any number between 1 to 9: "))

        if guess==target:
            print("wow, you guessed it right!")
            break
        else:
            print("your guess is wrong!")
guess_num()

# Write a Python program that accepts a word from the user and reverses it.
def reverseword():
    rev=input("enter a word: ")
    print("Reversedword: ", rev[::-1])
reverseword()
'''next method'''
def reversemethod():
    rev=input("Enter a word: ")
    for char in range(len(rev)-1,-1,-1):
        print(rev[char],end=' ')
reversemethod()
print("\n")

# Write a Python program to count the number of even and odd numbers in a series of numbers
def count_even_odd(num):
    odd=0
    even=0
    for i in num:
        if i%2==0:
            even+=1
        else:
            odd+=1
    print("Even",even)
    print("odd",odd)
num=[1,2,3,4,5,23,9,10]
count_even_odd(num)



# Write a Python program that prints each item and its corresponding type from the following list.
def item_and_type():
    datalist = [1452, 11.23, 1 + 2j, True, 'helooworld', (0, -1), [5, 12], {"class": 'V', "section": 'B'}]
    for item in datalist:
        print("The Type of", item , "is", type(item))
item_and_type()

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6
def printing_num():
    for i in range(1,6):
        if (i==3) or (i==6):
            continue
        print(i)
printing_num()

# Write a Python program to get the Fibonacci series between 0 and 50.
def fibonacci_series():
    x=0
    y=1
    while y<50:
        print(y)
        x=y
        y=x+y
fibonacci_series()

















