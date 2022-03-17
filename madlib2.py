f = open("madlb.txt", "r")

madlib = ""

for x in f:
    if x.startswith("*"):
        text = input("Give me a(n): " + x[1:].strip())
