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

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
# }

# car["color"] = "red"
# car["year"] = 2020
# x = car.items()
# print(x)

# if "model" in car:
#     print("Yes, 'model' is one of the keys in the thisDict dictionary")

# car["year"] = 2018
# car.update({"year": 2020})
# car.popitem()
# del car["model"]
# car.clear()
# print(car)

# for x, y in car.items():
#     print(x, y)

# myCar = dict(car)
# print(myCar)

# myFamily = {
#     "child1": {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Tobias",
#         "year": 2007
#     },
#     "child3": {
#         "name": "Linus",
#         "year": 2011
#     }
# }
# child1 = {
#     "name": "Emil",
#     "year": 2004
# }
# child2 = {
#     "name": "Tobias",
#     "year": 2007
# }
# child3 = {
#     "name": "Linus",
#     "year": 2011
# }
# myFamily = {
#     "child1": child1,
#     "child2": child2,
#     "child3": child3
# }

# print(myFamily)

# a = 33
# b = 200
# c = 500
# x = 41

# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")

# if a > b: print("a is greater than b")

# print("A") if a > b else print("B")

# if a > b or a > c:
#     print("At least one of the conditions is True")

# if x > 10:
#     print("Above ten,")
#     if x > 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20.")

# if b > a:
#     pass

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

# for x in "banana":
#     print(x)

# for x in fruits:
#     print(x)
#     if x == "banana":
#         break

# for x in fruits:
#     if x == "banana":
#         break
#     print(x)

# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

# for x in range(6):
#     print(x)

# for x in range(2, 6):
#     print(x)

# for x in range(2, 30, 3):
#     print(x)

# for x in range(6):
#     print(x)
# else:
#     print("Finally finished!")

# for x in range(6):
#     if x == 3: break
#     print(x)
# else:
#     print("Finally finished!")

# adj = ["red", "big", "tasty"]

# for x in adj:
#     for y in fruits:
#         print(x, y)

# for x in [0, 1, 2]:
#     pass

# def my_function():
#     print("Hello from a function")

# my_function()

# def func1(fname):
#     print(fname + " Refsnes")

# func1("Emil")
# func1("Tobias")
# func1("Linus")

# def func2(fname, lname):
#     print(fname + ' ' + lname)

# func2("Emil", "Refsnes")

# def func3(*kids):
#     print("The youngest child is " + kids[2])

# func3("Emil", "Tobias", "Linus")

# def func4(child3, child2, child1):
#     print("The youngest child is " + child3)

# func4(
#     child1 = "Emil",
#     child2 = "Tobias",
#     child3 = "Linus"
# )

# def func5(**kid):
#     print("His last name is " + kid["lname"])

# func5(
#     fname = "Tobias",
#     lname = "Refsnes"
# )

# def func6(country = "Norway"):
#     print("I am from " + country)

# func6("Sweden")
# func6("India")
# func6()
# func6("Brazil")

# def func7(food):
#     for x in food:
#         print(x)

# fruits = ["apple", "banana", "cherry"]
# func7(fruits)

# def func8(x):
#     return 5 * x

# print(func8(3))
# print(func8(5))
# print(func8(9))

# def func9():
#     pass

# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# x = lambda a : a + 10
# print(x(5))

# x1 = lambda a, b: a * b
# print(x1(5, 6))

# x2 = lambda a, b, c: a + b + c
# print(x2(5, 6, 2))

# def func1(n):
#     return lambda a: a * n

# mydoubler = func1(2)
# print(mydoubler(11))

# mytripler = func1(3)
# print(mytripler(11))

# cars = ["Ford", "Volvo", "BMW"]
# x = cars[0]
# print(x)

# cars[0] = "Toyota"
# print(cars)

# x1 = len(cars)
# print(x1)

# for x in cars:
#     print(x)

# cars.append("Honda")
# print(cars)

# cars.pop(1)
# cars.remove("Volvo")
# print(cars)

# class MyClass:
#     x = 5

# p1 = MyClass()
# print(p1.x)

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    
    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

p1.myfunc()

p1.age = 40
del p1.age
print(p1.age)