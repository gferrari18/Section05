f = open("myfile.txt", "r")
lineno = 1
for line in f:
    print(str(lineno) + ": " + line.strip())
    lineno = lineno +1
f.close()