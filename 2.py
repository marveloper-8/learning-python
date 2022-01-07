# import mymodule as mx
# import platform

# a = mx.person1["age"]
# print(a)

# x = platform.system()
# print(x)

# x1 = dir(platform)
# print(x1)

# from mymodule import person1
# print(person1["age"])

# import datetime

# a = datetime.datetime.now()
# print(a)
# print(a.year)
# print(a.strftime("%A"))

# b = datetime.datetime(2020, 5, 17)
# print(b)

# c = datetime.date(2018, 6, 1)
# print(c.strftime("%B"))

# print(a.strftime("%a"))
# print(a.strftime("%A"))
# print(a.strftime("%w"))
# print(a.strftime("%d"))
# print(a.strftime("%b"))
# print(a.strftime("%B"))
# print(a.strftime("%m"))
# print(a.strftime("%y"))
# print(a.strftime("%Y"))
# print(a.strftime("%H"))
# print(a.strftime("%I"))
# print(a.strftime("%p"))
# print(a.strftime("%M"))
# print(a.strftime("%S"))
# print(a.strftime("%f"))
# print(a.strftime("%j"))
# print(a.strftime("%U"))
# print(a.strftime("%W"))
# print(a.strftime("%c"))
# print(a.strftime("%C"))
# print(a.strftime("%x"))
# print(a.strftime("%X"))
# print(a.strftime("%%"))
# print(a.strftime("%G"))
# print(a.strftime("%u"))
# print(a.strftime("%V"))

# a = min(5, 10, 25)
# b = max(5, 10, 25)
# print(a)
# print(b)

# c = abs(-7.25)
# print(c)

# d = pow(4, 3)
# print(d)

# import math

# e = math.sqrt(64)
# print(e)

# f = math.ceil(1.4)
# g = math.floor(1.4)
# print(f)
# print(g)

# h = math.pi
# print(h)

# import json

# a = '{"name": "John", "age": 30, "city": "New York"}'
# b = json.loads(a)
# print(b["age"])

# c = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# d = json.dumps(c)
# print(d)

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# e = {
#     "name": "John",
#     "age": 30,
#     "married": True,
#     "divorced": False,
#     "children": ("Ann","Billy"),
#     "pets": None,
#     "cars": [
#         {"model": "BMW 230", "mpg": 27.5},
#         {"model": "Ford Edge", "mpg": 24.1}
#     ]
# }

# print(json.dumps(e))
# print(json.dumps(e, indent=4))
# print(json.dumps(e, indent=4, separators=(". ", " = ")))
# print(json.dumps(e, indent=4, sort_keys=True))

# import re

# txt = "The rain in Spain"
# txt2 = "That will be 59 dollars"
# txt3 = "hello planet"
# txt4 = "The rain in Spain falls mainly in the plain!"
# txt5 = "8 times before 11:45 AM"

# a = re.search("^The.*Spain$", txt)

# if a:
#     print("YES! We have a match!")
# else:
#     print("No match")
# b = re.findall("[a-m]", txt)
# print(b)

# c = re.findall("\d", txt2)
# print(c)

# d = re.findall("he..o", txt3)
# print(d)

# e = re.findall("^hello", txt3)
# if e:
#     print("Yes, the string starts with 'hello'")
# else:
#     print("No match")

# f = re.findall("planet$", txt3)
# if f:
#     print("Yes, the string ends with 'planet'")
# else:
#     print("No match")

# g = re.findall("he.*o", txt3)
# print(g)

# h = re.findall("he.+o", txt3)
# print(h)

# i = re.findall("he.?o", txt3)
# print(i)

# j = re.findall("he.{2}o", txt3)
# print(j)

# k = re.findall("falls|stays", txt4)
# print(k)
# if k:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# l = re.findall("\AThe", txt)
# print(l)
# if l:
#     print("Yes, there is a match!")
# else:
#     print("No match")

# m = re.findall(r"\bain", txt)
# print(m)
# if m:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# n = re.findall(r"ain\b", txt)
# print(n)
# if n:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# o = re.findall(r"\Bain", txt)
# print(l)
# if o:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# p = re.findall(r"ain\B", txt)
# print(p)
# if p:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# q = re.findall("\d", txt)
# print(q)
# if q:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# r = re.findall("\D", txt)
# print(r)
# if r:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# s = re.findall("\s", txt)
# print(s)
# if s:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# t = re.findall("\S", txt)
# print(t)
# if t:
#     print("Yes, there is at least one")
# else:
#     print("No match")

# u = re.findall("\w", txt)
# print(u)
# if u:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# v = re.findall("\W", txt)
# print(v)
# if v:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# w = re.findall("Spain\Z", txt)
# print(w)
# if w:
#     print("Yes, there is a match!")
# else:
#     print("No match")

# x = re.findall("[arn]", txt)
# print(x)
# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# y = re.findall("[a-n]", txt)
# print(y)
# if y:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# z = re.findall("[^arn]", txt)
# print(z)
# if z:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# aa = re.findall("[0123]", txt)
# print(aa)
# if aa:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# ab = re.findall("[0-9]", txt5)
# print(ab)
# if ab:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# ac = re.findall("[0-5][0-9]", txt5)
# print(ac)
# if ac:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# ad = re.findall("[a-zA-Z]", txt5)
# print(ad)
# if ad:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# ae = re.findall("[+]", txt5)
# print(ae)
# if ae:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")

# af = re.findall("ai", txt)
# print(x)

# ag = re.findall("Portugal", txt)
# print(ag)

# ah = re.search("\s", txt)
# print("The first white-space character is located in position:", ah.start())

# ai = re.search("Portugal", txt)
# print(ai)

# aj = re.split("\s", txt)
# print(aj)

# ak = re.split("\s", txt, 1)
# print(ak)

# al = re.sub("\s", "9", txt)
# print(al)

# am = re.sub("\s", "9", txt, 2)
# print(am)

# an = re.search("ai", txt)
# print(an)

# ao = re.search(r"\bS\w+", txt)
# print(ao.span())
# print(ao.string)
# print(ao.group())

# import camelcase

# c = camelcase.CamelCase()

# txt = "hello world"
# print(c.hump(txt))

# try:
#     print(x)
# except:
#     print("An exception occured")

# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("Something else went wrong")

# try:
#     print(x)
# except:
#     print("Something went wrong")
# finally:
#     print("The 'try except' is finished")

# try:
#     f = open("demofile.txt")
#     try:
#         f.write("Lorum Ipsum")
#     except:
#         print("something went wrong when writing to the file")
#     finally:
#         f.close()
# except:
#     print("Something went wrong when opening the file")

# a = -1

# if a < 0:
#     raise Exception("Sorry, no numbers below the zero")

# b = "hello"
# if not type(b) is int:
#     raise TypeError("Only integers are allowed")

# username = input("Enter username:")
# print("Username is: " + username)

price = 49
a = "The price is {} dollars"
print(a.format(price))

b = "The price is {:.2f} dollars"
print(b.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

myorder2 = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder2.format(quantity, itemno, price))

age = 36
name = "John"
c = "His name is {1}. {1} is {0} years old."
print(c.format(age, name))

d = "I have a {carname}, it is a {model}."
print(d.format(carname = "Ford", model = "Mustang"))