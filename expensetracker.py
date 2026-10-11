print("-----------Welcome to my Expense Tracker!-------------")

answers = [1,2,3,4] # this is the list of acceptable answers

def command_1():
    #this function stores our data in the text file
    item = input("Add item: ")
    price = input("Add price: ")
    arxeio = open("expenses_saved.txt",'a')
    arxeio.write(f"{item}-{price}\n")
    arxeio.close()
    


def command_2():
    #this function is used to print all the expenses items with their prices
    arxeio = open("expenses_saved.txt",'r')
    lines = arxeio.readlines()
    arxeio.close()
    if lines: # first safety check incase the user has no expenses
        for line in lines:
            line = line.strip()
            if not line: #double check incase there is an empty line 
                continue
            item,price = line.split("-",1)
            print("The ",item," costed ",price)

    else:
        print("You have no expenses!")


def command_3():
    #this function is used to show the users total expenses
    arxeio = open("expenses_saved.txt",'r')
    lines = arxeio.readlines()
    arxeio.close()
    if lines: # first safety check incase the user has no expenses
        sum = 0
        for line in lines:
            line = line.strip()
            if not line: #double check incase there is an empty line 
                continue
            item,price = line.split("-",1)
            price = float(price)  
            sum = sum + price
        print("Your total expense is: ",sum)
    else:
        print("You have no expenses!")

    

#printing the command choices to the user   
print("Press 1 to add an expense")
print("Press 2 to see all your expenses")
print("Press 3 to see the summarize of your expenses")
print("Press 4 to exit")

while True: # this is the main loop
    while True: # this loop is used to make sure we will have a correct command
        answer = int(input("Type command: "))
        if answer not in answers:
            print("Wrong command!")
        else:
            break

    if answer == 1:
        command_1()

    elif answer == 2:
        command_2()

    elif answer == 3:
        command_3()
    else:
        break
