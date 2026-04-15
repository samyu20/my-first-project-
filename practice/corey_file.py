a='java'
print(a)

house='stark','targeryen','lannister','baratheon','tyrel'

for i in house:
    print(i)

house='tyrel'
if house=='stark':
    print(" right house house")
elif house=='tyrel':
    print("welcome tyrel")
else:
    print("try again")

nums=[1,2,3,4,5]
for num in nums:
    if num == 4:
        print("found !")
        continue
    print(num)

nums=[1,2,3,4,5]
for num in nums:
    for letter in 'abc':
       print(num,letter)

x=0
while x < 10:
    if x ==6:
        break
    print(x)
    x+=1


def hi():
    return 'hi samy!'
print(hi())

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
course=['math','med']
info={'name':'Sam' , 'age':23,'hobby':'draw' }

student_info(*course,**info)

'''slicing strings'''

my_list=  [0, 1, 2, 3, 4, 5, 6, 7]
        #  0, 1, 2, 3, 4, 5, 6, 7
        # -8,-7,-6,-5,-4,-3,-2,-1
#list[start:end:stop]
print (my_list[: :-1])

sample= 'www.bangtanworld.com'
print(sample)
print(sample[::-1])  #reverse a string
print(sample[-4:])   #slicing specific word
print(sample[4:])
print(sample[4:-4])

'''list comperhension'''
nums=[1,2,3,4,5,6,7,8,9,10]

#'n' for each 'n' in nums
my_list =[]
for n in nums:
    my_list.append(n)
print(my_list)

my_list= [n for n in nums]           #list comperhension
print(my_list)

# 'n*n' for each 'n' in nums
my_list =[]
for n in nums:
    my_list.append(n*n)
print(my_list)

my_list=[n*n for n in nums]         #list comperhension
print(my_list)

# 'n' for each nin nums if n is even
my_list=[]
for n in nums:
    if n%2==0:
        my_list.append(n)
print(my_list)

my_list=[n for n in nums if n%2==0]     #list comperhension
print(my_list)

#pair for each number to letter 'abcd' and '0123'
my_list=[]
for num in range(4):
    for letter in  "abc":
        my_list.append((num,letter))
print(my_list)

my_list=[(num,letter) for num in range(1,4) for letter in 'abc']    #list comperhension
print(my_list)


house= ["Stark", "Lannister", "Targaryen", "Greyjoy"]
king = ["Robb", "Joffrey ", "Aegon", "Balon"]

# my_dict={}
# for houses, kings in zip(house,king):
#     my_dict[houses]=kings
# print(my_dict)

my_dict={houses:kings for houses, kings in zip(house,king )}     #list comperhension
print(my_dict)






