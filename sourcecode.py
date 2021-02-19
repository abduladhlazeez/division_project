# division_project
This contains the program that allows users to check if a number is divisible by certain numbers.
# Takes a value from the user and decides wether it is divisible based on
# another number obatined from the user
# GNU Open Source License
# Abdul Adhl Azeez

# Prompting the user for an input that is not greater than 3
usage = int(input("Select the number of divisors: "))
while usage  > 3:
    print("Sorry Maximum value is 3!")
    usage = int(input("Select the number of divisors: "))

if usage == 1:
    div_list = []
    turn1 = int(input("How many numbers do you want to divide? "))
    div_a = int(input("Enter the divisor to divide by : "))
    values = []
    for i in range(turn1):
        values.append(int(input(f"Enter Number {i + 1}: ")))
    for j in range(turn1):
        # Copying the values if divisible to a new list and printing that out
        if values[j] % div_a == 0:
            div_list.append(values[j])

    if len(div_list) == 0:
        print(f"Nothing is divisible by {div_a}")
    else:
        print(f"Numbers that can be divided by {div_a} : {div_list}")

elif usage == 2:
    div_list = []
    turn2 = int(input("How many numbers do you want to divide? "))
    div_a = int(input("Enter the first divisor to divide by : "))
    div_b = int(input("Enter the second divisor to divide by : "))
    values = []
    for i in range(turn2):
        values.append(int(input(f"Enter Number {i + 1} : ")))
    for j in range(turn2):
        # Copying the values to a new list if divisible and than if divisible giving the output
        if values[j] % div_a == 0 and values[j] % div_b ==0:
             div_list.append(values[j])
    if len(div_list) == 0:
        print(f"Nothing can be divided by {div_a} and {div_b}")
    else:
        print(f"Numbers that can be divided by {div_a} and {div_b} : {div_list}")


elif usage == 3:
    div_list = []
    turn3 = int(input("How many numbers do you want to divide? "))
    div_a = int(input("Enter the first divisor to divide by : "))
    div_b = int(input("Enter the second divisor to divide by : "))
    div_c = int(input("Enter the third divisor to divide by : "))
    values = []
    for i in range(turn3):
        values.append(int(input(f"Enter Number { i + 1} : ")))
    for j in range(turn3):
        # Copying the values to a new list if divisible and then printing the values which are divisble.
        if values[j] % div_a == 0 and values[j] % div_b ==0 and values[j] % div_c ==0:
             div_list.append(values[j])
    if len(div_list) ==0:
        print(f"Nothing can be divided by {div_a}, {div_b} and {div_c}")
    else:
     print(f"Numbers that can be divided by {div_a} and {div_b} and {div_c} : {div_list}")

else:
    print("Enter 1, 2 or 3")
