# Have the function BracketMatcher(str) take the str parameter being passed and 
# return 1 if the brackets are correctly matched and each one is accounted for.  Otherwise return 0. 
# For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" 
# the the output should be 0 because the brackets do not correctly match up. 
# Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

# Since we only care about standard round parantheses ( and ), we do not need a full stack data structure.
# 1. Start count = 0 
# 2. Iterate through every character in string.
# 3. When you see ( , increment count by 1 ---> count = count + 1
# 4. When you see ) , decrement count by 1 ---> count = count - 1
# If count becomes negative (-1), it means a closing bracket ) appeared with a matching opening bracket (
# After checking the whole string, if count == 0, all brackets were matched pair

def BracketMatcher(strParam : str) -> int:
    bracket_count = 0 
    
    for char in strParam:
        if char == "(":
            bracket_count += 1
        elif char == ")":
            bracket_count -= 1
        
        # If count drops below 0, a closing bracket came too early
        
        if bracket_count < 0:
            return 0
    
    if bracket_count == 0:
        return 1
    else: 
        return 0 
    
print(BracketMatcher("(hello(world))"))
print(BracketMatcher("((hello(world))"))

def BracketMatcher(strParam):

BracketMatcher(input())