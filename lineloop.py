f = open("myfile.txt", "r")
linenumber = 1
for line in f:
    print(str(linenumber) + ": " + line.strip())
    linenumber = lineno +1
f.close()