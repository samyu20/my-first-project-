idol ={
    "name": "jk",
    "age":26,
    "awards": True,
    "talents" : ["vocal","visual","dance","rap"]}
print(idol) #printing dictionary values
print(type(idol))
print(len(idol))
idol["age"]=25 #chaning the value of age
print(idol)
idol["country"]="south korea" #adding an item
print(idol)
idol.pop("awards")  # removing specified index by value
print(idol)
print("////////////METHOD/////////////////////////")
#DICIONARY METHOD
idol ={
    "name": "RM",
    "age":29,
    "awards": True,
    "talents" : ["lyricist","dance","rap"]}

x = idol.copy() #copy method
print("copy dict:",x)

y=1 #fromkey() #DOUBT
x= dict.fromkeys(x,y)
print(x)

i = idol.get("talents") #getting specified index value #get method()
print("specified items:",i)

i = idol.items() #returns as tuple in list, #item method() ,
print(i)

i = idol.keys()#getting key item in dict
print ("key items:",i)

i = idol.values() #getting value items
print("value items:",i)

idol.pop("awards") #removing an item
print("removed dict:",idol)
print()
#update method
idol.update({"albums":"luv ur self"})
print("updated dict:", idol)
#SETDEAFAULT DOUBT !
print()
#clear() method
idol.clear()
print(idol)





















