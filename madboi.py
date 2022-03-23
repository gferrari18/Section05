f = open("madlb.txt", "r")

story = ""

for line in f:
    if line.startswith("*"):
        text = input("Give me a(n) " + line[1:].strip() + ": ")
    else:
        text = line

    story = story + " " + text.strip()

print(story)

f.close()

f = open("madlb2.txt", "w")
f.write(story)
f.close