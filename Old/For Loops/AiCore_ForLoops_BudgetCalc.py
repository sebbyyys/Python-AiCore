#tuples list
order_list = [("tom", 7.87, 4),
              ("sug", 1.09, 3),
              ("ws", 0.29, 4),
              ("juc", 1.89, 1),
              ("fo", 1.29, 2)]

# This dictionary gives the full name of each product code.
names = {"tom": "Tomatoes",
         "sug": "Sugar",
         "ws": "Washing Sponges",
         "juc": "Juice",
         "fo": "Foil"}

budget = 10.00
running_total = 0
receipt = []
totalPrice = 0

# TODO - Loop through the order list
for orders in order_list:
    for i in names.keys():
    # TODO - Get the full name of the item
        if orders[0] == i:
            x = []
            x = names.get(orders[0])
    # TODO - Get the price of the item
    itemPrice = orders[1]*orders[2]
    #calculates total price
    totalPrice += itemPrice

    # TODO - Check if you still have enough money
    if totalPrice < budget:
        # TODO - If you can afford it, add the item to the receipt
        receipt.append(str(orders[2]) + " " + x)
        receipt.append(round(itemPrice, 2))
        print(receipt)
        print(f"The total of the receipt is : {totalPrice}")
    # TODO - If you can afford it, add the price of the item to the running total
    else:
        running_total += itemPrice
        print(f"Cant Afford {x}. Your running total for items remaining is: {round(running_total, 2)}")
    

    # TODO - If you can't afford it, print a message
        # TODO - If you can't afford it, print a message
        # TODO - If you can't afford it, break out of the loop