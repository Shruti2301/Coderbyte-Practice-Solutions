# Problem : Return n! (the product of all integers from 1 to n). (Took 10 mins to solve)

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

# Time Complexity : O(N) - makes n function calls down to 1
# Space Complexity : O(N) - holds n function calls in memory simulatenously