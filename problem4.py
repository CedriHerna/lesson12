#File 4 (problem4.py):

#Given an integer n, return a string array answer where:

#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.
def fizzbuzz(n: int):                #Giving the function of interger n
    answer = []                    #answer/product
    for i in range(1, n + 1)  :
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")   #doing the math
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")   #use append to add it to the product answer
        else:
            answer.append(str(i))
    return answer
n = 5
result = fizzbuzz(n)   #product end result
print (result)
