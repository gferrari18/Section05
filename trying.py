name = input("Enter your name: ")
filename = str(name) + ".txt"

f = open(str(filename), "r")
text = f.read()
print(text)

