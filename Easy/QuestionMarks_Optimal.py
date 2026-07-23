# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. 
# If so, then your program should return the string true, otherwise it should return the string false. 
# If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.
# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

# What are we given?
# We are given a string containing Digits (0-9), Letters (a-z, A-Z), Question Marks(?)
#
# What is the problem asking?
# For every pair of consecutive digits encountered while scanning the string: 
# - If the two digits add up to 10, there must be 3 question marks between them
# - If any such pair has less or anything other than 3 question marks (???), we need to return False
# - If there are no pairs summing to 10, return False
# - Otherwise, return True
#
# Key Observations: 
# Letters do not matter here.
# In this problem, we care about digits and question marks and no need to compare every digit to each other
# While scanning, we can remember the last digit we saw and number of ques marks after it,

# Optimal Approach : O(n)
# Instead of storing all digits and comparing every pair,
# scan the string only once while maintaining: 
# - previous digits
# - number of question marks
# - whether we have found a valid pair

# While Brute Force remembers all digits and repeatedly compares them and rescans the string.
# The Optimal Approach remembers only the last digit, the question mark count, and whether a valid pair has been found or not. 
# This reduces the time complexity from cubic to linear

def QuestionsMarks(strParam):
    
    # Store the previous digit encountered while scanning
    last_digit = None
    question_count = 0 
    
    # Count the number of question marks seen after the previous digit
    # Track whether we have found at least one pair summing to 10
    found_pair = False
    
    # Traverse the string from left to right only once
    for ch in strParam:
        
        # If we encounter a question mark,
        # Increment the count since the last digit
        if ch == '?':
            question_count = question_count + 1
            
        # Ignore letters and process only digits
        elif ch.isdigit():
            
            # Convert the digit character to an integer
            digit = int(ch)
            
            # If we have already seen a previous digit, 
            # compare it with the current digit
            if last_digit is not None:
                
                # Check whether the two digits sum to 10
                if last_digit + digit == 10:
                    
                    found_pair = True
                    
                    # The pair is invalid if there are
                    # not exactly three question marks between them
                    if question_count != 3:
                        return False
                    
            # Make the current digit the new previous digit
             # for the next comparison
            last_digit = digit
           
           # Reset the question mark count
            question_count = 0
     
    # Return False if no pair summing to 10 was found
    return found_pair

test_cases = [
    ("arrb6???4xxbl5???eee5", True),
    ("5??5", False),
    ("9???1", True),
    ("6??4", False),
    ("abc123", False),
]

for string, expected in test_cases:
    result = QuestionsMarks(string)
    print(f"Input: {string}")
    print(f"Expected: {expected}, Got: {result}")
    print("-" * 40)