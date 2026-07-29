# Count how many integers from 1 to n are divisible by 3 or 5
# Example: n = 10 -> 5 integers (In 1 to 10 : Divisible by 3 = 3,6,9 and Divisible by 5 = 5,10 so in total = 5 so we return 5)

def checkdivisibility(nums):
    
    count = 0
    for i in range(1,nums+1):
        if i % 3 == 0 or i % 5 == 0:
            count = count + 1
    return count 

usernumber = int(input('Enter a number:'))
print(checkdivisibility(usernumber))