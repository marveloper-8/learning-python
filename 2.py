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

import json

a = '{"name": "John", "age": 30, "city": "New York"}'
b = json.loads(a)
print(b["age"])

c = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
d = json.dumps(c)
print(d)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

e = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(e))
print(json.dumps(e, indent=4))
print(json.dumps(e, indent=4, separators=(". ", " = ")))
print(json.dumps(e, indent=4, sort_keys=True))