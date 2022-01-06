import mymodule as mx
import platform

a = mx.person1["age"]
print(a)

x = platform.system()
print(x)

x1 = dir(platform)
print(x1)

from mymodule import person1
print(person1["age"])