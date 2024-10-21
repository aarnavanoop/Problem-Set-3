def check_int(amount):
    while True:
        x,y = amount.split("/")
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print("Invalid! Please enter integer values")
            amount = input("What is the amount of fuel?: ")
        else:
            break
        
    return x,y


def greater_or_not(a,b):
    while True:
        if a > b:
            print("Invalid! Please make sure the numerator is smaller than the denominator")
            fuel = input("What is the amount of fuel?: ")
            a,b = fuel.split("/")
        elif b == 0:
            print("Invalid! Please make sure the denominator is 0 ")
            fuel = input("What is the amount of fuel?: ")
            a,b = fuel.split("/")
        else:
            a = int(a)
            b = int(b)
            return a,b

def output(a,b):
    percentage = (a/b)*100
    percentage = round(percentage)

    if 99 > percentage > 1:
        print(f"{percentage}%")
    elif percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")

def main():
    #get user input
    fuel = input("What is the amount of fuel?: ") 
    
    #check if it is a valid integer
    x,y = check_int(fuel)

    #check if x is greater than y and that y != 0
    x,y = greater_or_not(x,y)


    #output the necessary result
    output(x,y)


main()