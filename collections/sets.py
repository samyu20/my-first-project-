birds = {"crow", "peacock", "swan"}
print(birds)
print(type(birds))

#set doesn't allow duplicate
birds = {"crow", "peacock", "swan", "swan"}
print(birds)

#True and 1 are same value
birds = {"crow", "peacock", "swan", True, 1, 2, 3, 50, "dove"}
print(birds)

#False and 0 are same value
birds = {"crow", "peacock", "swan",0,False, 2, 3, 50, "dove"}
print(birds)
print(len(birds))

#add item
birds1 = {"crow", "peacock", "swan", }
birds2=["hen"]
birds1.add("parrot")
print(birds1)

#updating other iterable to set
birds1.update(birds2)
print(birds1)

#remove
birds1.remove("crow")
print(birds1)
#pop

mytuple= {"crow", "peacock", "swan", 2, 3, 50, "dove","love","peace"}
x=mytuple.pop()
print(x)

#removed item-randomly
print(mytuple)
mytuple.clear()
print("cleared set:",mytuple)


'''SET METHODS'''
pro={"python","java","c","c++","json"}
pro.add("javascript") #adding element
print(pro)
pro.copy() #copying set
print(pro)

#difference method()
a={"cat","dog","mouse"}
b={"elephant","mouse","monkey"}
c={"cow","goat","dog"}
d=a.difference(b) #same value in a,b will be removed,printing a set ,a-b
print(d)
e=c-b-a # c.difference(b,a)
print(e)

#difference update
a -=b
print(a)
b -=c | a  #DOUBT! in update difference and intersection
print(b)

#discard method
a.discard("mouse")
print("after removing mouse:",a)

#intersection method
x= {"cat","dog","goat","crow"}
y= {"java", "python" ,"c","cat"}
z= {"goat","crow","dove","python","cat"}
result=x.intersection(y)
print(result)
r1=y&z
print(r1)
r2=x & z
print(r2)
r3= x & y & z
print(r3)

#isdisjoint()
a= {"cat","dog"}
b= {"java","python" ,"c","cat"}
k = {"cat","yellow","dog"}
c= a.isdisjoint(b) #no one items same a, b it will be TRUE
print(c)

#issubset
c= a.issubset(b) # if all a value present in two set it will be TRUE
print(c)
c = a <= k
print(c)

#issuperset
d = k.issuperset(b)
print(d)
d= k.issuperset(a)
print(d)

#symmetric differnce (same value in set will removed , else all item will print)
i={"python","java","c"}
j={"goat","crow","python","cat"}
k = i ^ j # i.symmetric_difference(j)
print(k)

#union two set values , duplicate count as one value
k = i.union(j)  # i | j
print(k)









