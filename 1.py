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
# thisList = ["apple", "banana", "cherry"]
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

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newList = []

# for x in fruits:
#     if "a" in x:
#         newList.append(x)

# newList = [x for x in fruits if "a" in x]
# newList = [x for x in fruits if x != "apple"]
# newList = [x for x in fruits]
# newList = [x for x in range(10)]
# newList = [x for x in range(10) if x < 5]
# newList = [x.upper() for x in fruits]
# newList = [x if x != "banana" else "orange" for x in fruits]

# def myfunc(n):
#     return abs(n - 50)

# thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thisList = [100, 50, 65, 82, 23]
# thisList.sort(key = myfunc)
# thisList = ["banana", "Orange", "Kiwi", "cherry"]
# thisList.sort(key = str.lower)
# thisList.reverse()
# myList = list(thisList)
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# for x in list2:
#     list1.append(x)
# list1.extend(list2)

# print(list1)

# thisTuple = ("apple", "banana", "cherry")
# if "apple" in thisTuple:
#     print("Yes, 'apple' is in the fruits tuple")

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# y = list(thisTuple)
# y.append("orange")
# thisTuple = tuple(y)

# y = ("orange",)
# thisTuple += y

# y = list(thisTuple)
# y.remove("apple")
# thisTuple = tuple(y)

# del thisTuple

# print(thisTuple)
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, *yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# for x in thisTuple:
#     print(x)

# for i in range(len(thisTuple)):
#     print(thisTuple[i])

# i = 0
# while i < len(thisTuple):
#     print(thisTuple[i])
#     i += 1

# thisSet = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# myList = ["kiwi", "orange"]
# print("banana" in thisSet)

# for x in thisSet:
#     print(x)

# thisSet.add("orange")
# thisSet.update(myList)
# thisSet.discard("banana")
# x = thisSet.pop()
# print(x)
# thisSet.clear()
# del thisSet
# print(thisSet)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# set1.update(set2)
# print(set1)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)
# x.symmetric_difference_update(y)
# print(x)

# z = x.intersection(y)
# z = x.symmetric_difference(y)
# print(z)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}

# car["color"] = "red"
# car["year"] = 2020
# x = car.items()
# print(x)

# if "model" in car:
#     print("Yes, 'model' is one of the keys in the thisDict dictionary")

# car["year"] = 2018
car.update({"year": 2020})
print(car)