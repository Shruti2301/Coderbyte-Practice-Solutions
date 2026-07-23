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

# Brute Force Approach
# 1. Extract all digits and their positions
# 2. Compare every pair of digits
# 3. If a pair sums to 10: 
# - Count the number of question marks between their positions
# - If it is not exactly 3 --> return False
# 4. If at least one valid pair exists ---> return True
# 5. Otherwise ===> return False
#
# The drawback of brute force approach is 
# O(n^3) time complexity and O(n) space complexity
def QuestionsMarks(strParam):

    # Store (digit, index)
    digits = []

    # Extract all digits and their indices
    for i, ch in enumerate(strParam):
        if ch.isdigit():
            digits.append((int(ch), i))

    found_pair = False

    # Compare every possible pair
    # (6,4), (6,5), (6,5), (4,5), (4,5), (5,5)
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):

            num1, idx1 = digits[i]
            num2, idx2 = digits[j]

            # Check if pair sums to 10
            if num1 + num2 == 10:

                found_pair = True
                question_count = 0

                # Count question marks between the two digits
                for k in range(idx1 + 1, idx2):
                    if strParam[k] == "?":
                        question_count += 1

                # Invalid pair
                if question_count != 3:
                    return False

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