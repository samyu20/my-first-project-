#list examples
flist=["red","yellow","blue"]
print(flist)

#printing duplicate values
slist=["red","yellow","blue","purple","blue"]
print(slist)

#length of list
thislist=["red","yellow","blue","purple","blue"]
print(len(thislist))

#data type
list1=["lilly",67, True, 'yellow']
print("data type:",list1)

#type
list2=["red","yellow","blue","purple","blue"]
print(type(list2))

# accessing,negative index, range of index
list2=["red","yellow","blue","purple","orange","black","white"]
print(list2[3])
print(list2[-3])
print(list2[2:5])
print(list2[:3])
print(list2[-6:-2])

#check if it exist
list3=["red","yellow","blue","purple","orange","black","white"]
if "purple" in list3:
    print("yes, purple is there!")

#change list items,#adding item
list4=["red","yellow","blue","purple","black","white"]
list4[4]="peach"
print(list4)
list4.append("green")
print(list4)
list4.insert(2,"golden")
print(list4)
color2=["orange","brown"]
list4.extend(color2)
print(list4)

#removing item
list4.remove("blue")
print(list4)
list4.pop(2)
del list4[1]
print(list4)
print("///////////FOR LOOP/////////////")
list5=["red","yellow","blue"]
for  k in list5:
    print(k)

#using range(), len()
list5=["red","orange","blue"]
for k in range(len(list5)):
    print(list5[k])
print("///////////WHILE LOOP/////////////")
list6=["purple","yellow","blue"]
k=0
while k < len(list6):
    print(list6[k])
    k = k+1

# LIST COMPRENSHENSION

print("////////LIST COMPREHENSION/////////")

#without list compherhension
color=["red","yellow","blue","purple","orange","black","white"]
newcolor=[]
for k in color:
    if "l" in k:
        newcolor.append(k)
print(newcolor)

#with list comperhension
color=["red","yellow","blue","purple","orange","black","white"]
newcolor=[i for i in color if "h" in i]
print(newcolor)
newcolor=[i for i in color if i!="blue"]
print(newcolor)
newcolor=[i for i in color]
print(newcolor)
newcolor= [i.upper() for i in color]
print(newcolor)
newcolor= ['sam' for i in color]
print(newcolor)
print("///////////SORT LIST///////////")

#ascending
flower=["rose","lilly","lotus","jasmine","tulip","sunflower"]
flower.sort()
print(flower)

#desecnding
flower.sort(reverse= True)
print(flower)

#numerical in ascending and desending
shopno=[23,67,69,9,39]
shopno.sort()
print(shopno)
shopno.sort(reverse = True)
print(shopno)
list2=["red","orange","yellow","blue"]
print (list2[1:4])
list2[1:4]=["purple","black","peach"]
print(list2)

'''LIST METHODS'''
#list methods
#append list
countries=["india", "germany","greece",]
countries.append("japan")
print(countries)
countries2=["usa","brazil"]
countries.append(countries2)
print(countries)

#clear method
countries2.clear()
print(countries2)

#copy
k = countries.copy()
print(k)

#count method
countries3=["india", "germany","greece","switzerland","india"]
i=countries3.count("india")
print("total n of india is :", i)

#extend method
points=[2,4,6,9,7,10,5,6]
countries3.extend(points)
print(countries3)

#index method
con4=["cuba","india","china"]
i = con4.index("china")
print("the index of china is:",i)
points=[2,4,6,9,7,10,5,6]
i= points.index(6,4)
print("the index of 6 is :", i)

#insert method
con4=["cuba","india","china"]
con4.insert(0,"canada")
print(con4)

#pop
con5=["india", "germany","greece","uk","hawai"]
con5.pop(1)
print(con5)
i = con5.pop(3)
print(i)

#remove, reverse and sort
con6=["india", "germany","greece","switzerland","bhutan"]
con6.remove("germany")
print(con6)
con6.reverse()
print("the reversed list:", con6)
con6.sort()
print("the sorted list:",con6)