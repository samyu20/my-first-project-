def print_numbers():
    for i in range(1,11):
        print(i)
print_numbers()


def num_prime(n):
    if n<2:
        return 'not prime number'
    for i in range(2,n):
        if n%i==0:
            return 'not prime number'
    return 'prime number'

ip=int(input("enter a value: "))
print(num_prime(ip))

'''count of even odd number in list'''
def even_odd_count (mylist):
    even=0
    odd=0
    for n in mylist:
        if n %2==0:
            even+=1
        else:
            odd+=1
    return even, odd

values=[11,23,44,55,78,90,17]
print (even_odd_count(values))

'''Armstrong number'''
def is_armstrong(n):
    sum=0
    digits=len(str(n))
    temp=n
    while temp >0:
        l_digit=temp%10
        sum=sum+l_digit**digits
        temp//=10

    if sum==n:
        return "armstrong"
    else:
        return "no armstrong"
n=int(input("enter a value:"))
print(is_armstrong(n))

'''for loop'''
def is_armstrong(num):
    sum=0
    digit=len(str(num))

    for d in str(num):
        sum+=int(d)**digit

    if sum==num:
        return "its an Armstrong number!"
    else:
        return "its not an Armstrong number!"

num=int(input("enter your value: "))
print(is_armstrong(num))

def even_num():
  for i in range (1,21):
    if i%2==0:
     print(i)
even_num()


def even_num(n):
    even=[]
    for i in range(2,n+1,2):
        even.append(i)
    return even
n=int(input("enter a number: "))
print(even_num(n))

print("The sqaure values are:", end=" ")
for i in range(1,7):
    print(i*i, end=" ")

def sum_Nnum(n):
    sum=0
    for i in range(1,n+1,1):
        sum+=i
    return sum
n=int(input("enter a number:"))
print(sum_Nnum(n))

for x in range(5):
    for y in range(x):
        print("*" , end="")
    print()



















