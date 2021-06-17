file = open("test.txt", "w")

a = file.write("asd")
print(a)
file.close()

file = open("test.txt", "r")
print(file.read())

file.close()
