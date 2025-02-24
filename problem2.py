
# To solve this problem I have to consider both a number that I input as well as the processes it takes to get there
# A factorial is a REPEATED multiplication of a number until it reaches 0, but doesn't multiply by zero. 
# Since I am repeating a value indefinetly (as it depends on the user input), I will be using a while loop.

# First I ask for a number
number = input("Hello! Please enter the number that you want us to factorial")

# Then I turn the input into an integer
number = int(number)


# Then I create this number so that I have a number that ticks down to stop the loop and will start from the number so that I can use it to create the factorial

count = number

# Loop the digit in a function that then returns the value after it gets factorialed

while(count > 1):
    number = number * (count - 1)
    count -= 1
    

# Then print the value to the screen for the user to see.
print(number)