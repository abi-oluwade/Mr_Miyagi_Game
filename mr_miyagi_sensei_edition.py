print ("Hello young grasshopper,")
# The 'while True' here means that the whole loop will run on forever/infinitely it will always be a true condition ,
# but can be broken with the use of the 'break' keyword after a condition has been met and will print the statement
# at the end outside the loop.
while True:
    user_input = str(input("what do you seek from me?"))
    substring1 = "?"

    if user_input.count(substring1) > 0:
        print("Questions are wise, but for now. Wax on, and Wax off!")
    # 'find' returns an integer representing the index of where the search item was found. If it isn't found,
    # it returns -1. And this can be used in conjunction with the while loop and if-elif statement to
    # print the appropriate response.
    elif user_input.find("Sensei") < 0 and user_input.find("sensei") < 0:
        print("You are smart, but not wise - address me as Sensei please")
    elif user_input.find("Block") > 0 or user_input.find("block") > 0:
        print("Remember, best block, not to be there..")
    elif user_input.find(" ") > 0 and user_input.find("Sensei, I am at peace"):
        print("Do not lose focus. Wax on. Wax off.")
    elif user_input ==  str("Sensei, I am at peace"):
        break
    # 'break' here is critical as it stops the loop from being infinite once the condition is satisfied.
print("Sometimes, what heart know, head forget")

# https://www.w3schools.com/python/python_conditions.asp
# https://www.w3schools.com/python/python_while_loops.asp
