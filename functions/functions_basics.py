def welcome():
    print(10)
welcome()

def hi():
    return 'welcome'
print(hi().upper()  )

def assign(a,b):
    print(a,b)
for i in[10,20,30]:
    assign(i,"value")

def calc_len(l):
    i=0
    while i <len(l):
        i+=1
    print(i)
calc_len((11,12,33,2))

def add(a,b=2):
    print(a-b)
for i in (9,5,6):
    add(i)

def adding(x):
    x=x+10
    return x
# print(adding(5))
output=adding(10)
print(output)

def is_even(a):
    if a%2==0:
        return 'its even number'
    return 'its not'
#print(is_even(5))
output=is_even(7)
print(output)

'''counter in function'''
def counter(x):
    i=1
    while i<=x:
        print(i)
        i+=1
counter(5)
def counter(x):
   for i in range(1, x+1):
    print(i)
counter(4)

'''reverse counter'''
def reverse_counter(b):
    while b >0:
        print(b)
        b-=1
reverse_counter(5)

def check(num):
    if num % 2 == 0:
        return "even"
    return "odd"

print(check(10))
print(check(7))

try:
    n= int (input("enter pin: "))
except:
    print("pin must be number")
else:
    print("entered pin is:",n)
finally:
    print("thank you")


def print_num():
  i=1
  while i<=10:
    print(i)
    i+=1
print_num()

def sum_of_num(N):
   i=0
   tot=0
   while i <=N:
       tot+=i
       i+=1
   return tot
N=int(input("enter ur num:"))
print(sum_of_num(N))

def even_num(N):
    i=2
    while i <=N:
        print(i)
        i+=2
even_num(10)

def even(N):
    for i in range (1,N+1):
        if i %2==0:
            print(i)
even(12)

def counter(i):
   while i>=1:
       print(i)
       i-=1
counter(5)


def myfunc():
    global x
x = "fantastic"
myfunc()
print(x)












































