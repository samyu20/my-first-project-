apps=("pinterest","whatsapp","youtube","whatsapp")
print("my tuple:",apps)
print(type(apps))
mytuple=apps*2
print(mytuple)

#tuple methods
#count method,
k = apps.count("whatsapp")
print(k)
sam_marks=(98,96,99,98,96,94,96,88)
i = sam_marks.count(96)
print("total num of 96:",i)
i = sam_marks.index(94)
print("index of 94:",i)
i = sam_marks.index(96)
print("index of 96:",i)

