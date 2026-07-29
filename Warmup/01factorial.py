# Problem : Return n! (the product of all integers from 1 to n).

# Factorial is product of all integers from 1 to n
# 3! = 3 x 2!

def factorial(nums):
    # Base Case : 0! = 1 and 1! = a
    if nums <= 1:
        return 1
    # Recursive Case 
    else:
        return nums * factorial(nums - 1)
    
usernumber = int(input('Enter a number:'))
print(factorial(usernumber))