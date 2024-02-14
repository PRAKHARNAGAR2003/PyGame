print("Hello")

# variables

data = 21
pi = 3.14
email = "prakhar.nagar@gmail.com"
eat = True

print(data)

# Input

# string
basketball_player = input("Who is my favorite basketball player")
print("My favorite basket player is" + basketball_player)

# logical operator
your_age = input("How old you are??")
birthyear = 2023 - int(your_age)
print(birthyear)

#Operation of strings
martiny = "I have programming and I will learn fast"
print(martiny.upper())
print(martiny.lower())
print(martiny.find("g"))
print(martiny.replace("Love","Just Like"))
print(martiny.find("programming"))

# Arithematic operation

x = 5
y = 11
print(y%x)
print(x**y)

x += y
print(x)

# Comparisions and Logical Operation
x = 5>4 
print(x)

x = 5<4
print(x)

x = 5 != 4
print(x)

x = 5==4

rent = 550
print(rent>50 or rent<100)
print(rent>50 and rent<1000)

# If-else loop
carspeed = 100
if(carspeed>100):
    print("You are driving too fast")
elif(carspeed<20):
    print("You are driving too slow, This is a highway")
else: 
    print("Your speed is good")

print("Ready")

# Data Structure

techlist = ["Apple", "Microsoft", "Samgsung", "Dell","Hp"]
print(techlist[0:2])

techlist[0] = "Tesla"
print(techlist)

techlist.remove("Samgsung")
print(techlist)

# techlist.insert("Tesla")
# print(techlist)

print(len(techlist))

techlist.clear()
print(techlist)

fruits = {"Banana":0.49,"Orange":1.5,"Apple":1.09}
fruits["Banana"] = 2.60
print(fruits)

# functions

def homework():
    print("Your homework task: ")
    print("Declare a variable in python")

print("Start")
homework()
print("End")

# Return Function

def path(v,t):
    print(v*t)
print(path(30,60))

# Exception
try:
    items = int(input("Type a number of items: "))
    total = 30
    price_per_item = total/items
    print(items)
