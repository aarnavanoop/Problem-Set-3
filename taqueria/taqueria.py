
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#user_item = input("What is the item?: ").title()
total = 0
while True:
    try:
        user_item = input("What is the item?: ").title()
    except EOFError:
        print()
        print("Program exited.\n")
        break
    else:
        if user_item in menu:
            total += menu[user_item]
            print(f"Total: ${total}")
        else:
            pass




        





