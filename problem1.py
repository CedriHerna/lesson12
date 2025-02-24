#We are going to create a function to reverse the order of a string

def reverse_string(): #create our function
    phrase = input("Enter a phrase: ")#take input from user to add a phrase (string)
    reverse_phrase = phrase[::-1]#process of reversing string, we slice it
    print(reverse_phrase) #finally print out the reversed string
reverse_string()    #call the function

