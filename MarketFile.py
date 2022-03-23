list = []
cart = []
item = ""
total = 0

while item != "none":
    item = input("enter item name, or none when done: ")
    if item != "none":
        list.append(item)

file = open("shoppinglist", "w")
for x in list:
    file.write(x + "\n")
file.close()

file = open("shoppinglist", "r")
linumber = 1
for line in file:
    print(line.strip())
    delete = input("Do you still need this item?: ")

print("Nice, go to the store!")

while len(list) != 0:
    item = input("Enter item name: ")
    if item in list:
        list.remove(item)
        price = float(input("enter item price: "))
        qty = int(input("enter price qty: "))
        evr = (item, price, qty)
        cart.append(evr)
    elif item not in list:
        print("You must enter an item that was previously added to the list!")

for x in cart:
    (item,price,qty) = x
    print("Item name: " + item + " Price: " + str(price) + " Qty: " + str(qty))
    total = total + (float(price) * int(qty))
print("Total = " + str(total))