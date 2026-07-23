# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. 
# For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.

# Input : "Hello World and Coders"
# Output : "sreddoC dna dlroW olleH"
#
# What are we given?
# - A string containing characters

# What is the problem asking?
# - Reverse the order of all characters in the string
# - Return the reversed string

# Key Observation
# - Python strings are immutable, meaning they cannot be modified in place
# - Therefore, we convert the string into a list of characters, reverse the list, and join it back into a string.

# Time Complexity : O(n) and Space Complexity : O(n)

def FirstReverse(strParam):

    # Convert the string into a list of characters
    charlist = list(strParam)

    # Reverse the list in place
    charlist.reverse()

    # Join the reversed characters back into a string
    return "".join(charlist)


# Test Cases
test_cases = [
    ("Hello World and Coders", "sredoC dna dlroW olleH"),
    ("hello", "olleh"),
    ("Python", "nohtyP"),
    ("a", "a"),
    ("", ""),
    ("12345", "54321")
]

for string, expected in test_cases:
    result = FirstReverse(string)

    print(f"Input    : {string}")
    print(f"Expected : {expected}")
    print(f"Got      : {result}")
    print(f"Result   : {'PASS' if result == expected else 'FAIL'}")
    print("-" * 40)