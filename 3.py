# f = open("demofile.txt", "r")
# print(f.read())
# print(f.read(5))
# print(f.readline())
# print(f.readline())

# for x in f:
#     print(x)

# f.close()

# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# f = open("demofile2.txt", "r")
# print(f.read())

# f = open("demofile3.txt", "w")
# f.write("Woops! I have new content!")
# f.close()

# f = open("demofile3.txt", "r")
# print(f.read())

# f = open("myfile.txt", "x")

import os
# os.remove("demofile.txt")
# if os.path.exists("demofile2.txt"):
#     os.remove("demofile2.txt")
# else:
#     print("The file does not exist")
os.rmdir("myfolder")