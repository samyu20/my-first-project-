x='orange'
def color():
    print(x)
color()

y='pink'
def color2():
    global y
    y='yellow'
color2()
print(y)

z='purple'
def clr():
  global z
  z='peach'
clr()
print(z)

k=("class")
def greeting():
    print("welcome to " +k)
greeting()

def myfunc():
    global x
x = "fantastic"
myfunc()
print(x)
