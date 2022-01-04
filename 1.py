# x = 5
# y = "John"
# print(type(x))
# print(type(y))

# x = str(3)
# y = int(3)
# z = float(3)

# print(x, y, z)

# x, y, z = "Orange", "Banana", "Cherry"
# x = y = z = "Orange"
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# x = "awesome"
# print("Python is " + x)

# x = "Python is "
# y = "awesome"
# z = x + y
# print(z)

# x = 5
# y = 10
# print(x + y)

# x = "awesome"

# def myfunc():
#     global x 
#     x = "fantastic"
#     print("Python is " + x)

# myfunc()

# print("Python is " + x)

# import random

# x, y, z = 1, 2.8, 1j
# print(type(x))
# print(type(y))
# print(type(z))

# print(random.randrange(1, 10))

# a = "Hello, World!"
# c = " Hello, World! "
# d = "Hello"
# e = "World"
# print(a[1])
# print(len(a))

# for x in "banana":
#     print(x)

# txt = "The best things in life are free!"
# if ("free" in txt):
#     print("Yes, 'free' is present.")

# if "expensive" not in txt:
#     print("No, 'expensive' is NOT present.")

# b = "Hello, World!"
# print(b[2:5])
# print(b[:5])
# print(b[2:])
# print(b[-5: -2])
# print(a.upper())
# print(c.strip())
# print(a.replace("H", "J"))
# print(a.split(","))

# f = d + " " + e
# print(f)

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {2} pieces of item {0} for {1} dollars."
# print(myorder.format(quantity, itemno, price))

# print(b.capitalize())
# print(b.casefold())

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 200
# b = 33

# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")

# class myclass():
#     def __len__(self):
#         return 0

# myobj = myclass()
# print(bool(myobj))

# def myFunction():
#     return True

# print(myFunction())

# if myFunction():
#     print("YES!")
# else:
#     print("NO!")

# x = 200
# print(isinstance(x, int))

# print(10 + 5)
# print(5 % 2)
# print(2 ** 5)
# print(5 ** 2)
# print(15 // 2)

# x = 5
# print(x += 3)

# thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thisList)
# print(len(thisList))
# print(thisList[1])
# print(thisList[-1])
# print(thisList[2:5])
# print(thisList[:4])
# print(thisList[2:])
# print(thisList[-4:-1])

# if "apple" in thisList:
#     print("Yes, 'apple' is in the fruits list")

# thisList[1:3] = ["watermelon"]
# thisList.insert(2, "watermelon")
thisList = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thistuple = ("kiwi", "orange")
# thisList.extend(thistuple)
# thisList.pop()
# del thisList
# thisList.clear()
# print(thisList)
# for x in thisList:
#     print(x)

# for i in range(len(thisList)):
#     print(thisList[i])

# i = 0
# while i < len(thisList):
#     print(thisList[i])
#     i += 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newList = []

# for x in fruits:
#     if "a" in x:
#         newList.append(x)

# newList = [x for x in fruits if "a" in x]
# newList = [x for x in fruits if x != "apple"]
newList = [x for x in fruits]

print(newList)