print('This program will ask you to guess a correct number')
target = 55
# obtain input from the user:
value = int(input("Enter an integer between 1 and 100: "))
if value > target:
    print("WRONG!", value, "is high/too high")
elif int(value) < target:
    print("WRONG!", value, "is low/too low")
else:
    print("YOU WIN!")