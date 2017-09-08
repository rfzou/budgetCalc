import time
import os

print(time.strftime("%H:%M"))
print(time.strftime("%d/%m/%Y"))

file = open("numbers.txt", "w+", 1)

print(file.closed)
print(file.mode)
print(file.name)

file.write("Hello world! \n")

filer = open("numbers.txt", "r+")
st1r = filer.read(9);

print(st1r)


file.close()
