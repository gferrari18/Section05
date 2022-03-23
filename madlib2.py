f = open("maddlb.txt", "r")

madlib = ""

for x in f:
    if x.startswith("*"):
        text = input("Give me a(n): " + x[1:].strip() + ": ")
    else:
        text = x

    madlib = madlib + " " + text.strip()

print(madlib)

f.close

f = open ("maddlb2.txt", "w")
f.write(madlib)
f.close
