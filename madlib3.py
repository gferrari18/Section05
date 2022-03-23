f = open("madlib3.txt", "r")
story = ""

for line in f:
    if line.startswith("*"):
        txt = input("Please enter a(n), " + line[1:].strip() ": "
    else
        txt = line
    story = story + " " + txt.strip()


    