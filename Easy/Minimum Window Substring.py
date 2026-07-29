from collections import Counter

def MinWindowSubstring(strArr):
    N, K = strArr[0], strArr[1]
    
    # Frequency map for characters needed from K
    need = Counter(K)
    required_unique = len(need)
    
    print("Character Counts Needed (need):", need)
    print("Number of Unique Characters (required_unique):", required_unique)
    
    # Count Character Frequencies needed from K
    # Create an empty dictionary (hash map) : We are using this to store each character
    # required from string K and how many times it needs to appear
    need = {}
    
    # Loops through string K, looking at one character at a time
    # need.get(char,0) : Looks inside the need dictionary for char
    for char in K:
        # If char is already in the dictionary --> return the current count
        # If char is NOT in the dictionary ---> .get(....,0) will safely return 0 instead of crashing
        # +1 adds 1 to that count and stores it back in need[char]
        
        # get() method is used to safely retrieve a value from a dictionary without causing the program to crash if the key does not exist
        # key : The specific key you want to look up
        # default : The value returned if the key is missing.
        need[char] = need.get(char,0) + 1
        
    # Initializes a empty string variable where we will store our winning(shortest) valid substring
    best_substring = ""
    
    # float('inf') represents infinity in Python - a number larger than any actual string
    min_len = float("inf")
    
    # left sets the starting point of left pointer to index 0
    left = 0
    
    # window is an empty dictionary that will track the characters currently in my sliding window
    window = {}
    
    # Helper function to check if window contains all the needed characters
    def is_valid():
        # Loops through each required character (char) and how many times it is needed (count) from our checklist (need)
        for char, count in need.items():
            
            # Looks inside our current window dictionary to check how many char we have
            # If we have fewer than count, the window needs missing required letters and it returnds False
            # However, it has exact count --> it will return True
            if window.get(char,0) < count: 
                return False
        # Every required char without failing? Return True!
        return True
    
    # Slide the right pointer
    # Start a loop that steps through every index of string N from index 0 till the end
    
    # The variable right acts as our right pointer, defining the right edge of sliding window
    for right in range(len(N)):
        
        # Pick out the element that is pointed by right index in N and put it in char 
        char = N[right]
        
        # Add the newly found character to our window dictionary
        # First we will check if char is already there in the window dictionary or not
        # If it is ==> We return the current count
        # It it is not ===> safely return 0 instead of raising an error
        # We add 1 to that returned value and store it back to window[char]
        window[char] = window.get(char,0) + 1
        
        # Whenever window is valid, try shrinking from the left
        
        # Run a loop that keeps repeating as long as the current window contains all char needed from K
        # We used while instead of if --> becaus eonce a window is valid, I will be able to remove multiple char from the left
        while is_valid():
            
            # Calculates how many characters are in the current valid window
            # Indices are 0-based. If left = 0 and right = 3, length is 3-0+1 = 4 characters
            current_length = right - left + 1
            
            # Record smaller window if found
            # Checks if this valid window is shorter than any valid window found earlier
            # If it is shorter - Update min_len to store this new record length
            # Extract the exact substring using Python slicing ( N[left: right + 1]) and saves it in best_substring
            if current_length < min_len:
                min_len = current_length
                best_substring = N[left : right + 1]
                
            # Remove left character and shrink
            # Decrements the count of the character at position left in our window 
            # If N[left] is 'a' and we currently have window['a'] = 2, it reduces window['a'] to 1.
            window[N[left]] -= 1
            
            # Moves the left pointer one step to the right
            # Physically shrinks the window from the left side
            left += 1
    
    # Returns the shortest valid substring that was recorded during the execution
    return best_substring
    

# Test it by passing a list with N and K
MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"])


# Example Walkthrough : 
# N is 'aabd' and K = 'ad' ( need 1 'a' and 1 'd')
# 1. R reaches index 3 ('aabd') : is_valid() becomes True
# -> current_length = right - left + 1 = 3 - 0 + 1 = 4
# -> min_len updated to 4, best_substring = "aabd"
# -> Kicks out N[0] ('a'), increments left to 1.

# Loop checks is_valid() again ('abd' at indices 1...3):
# Still has 1 'a' and 1 'd', so is_valid() is still True!
# current_length = 3 - 1 + 1  = 3
# -> 3 < 4 : min_len updated to 4, best_substring = "abd"
# -> Kicks out N[1] ('a') and increments left to 2
# -> Loop checks is_valid() again ('bd' at indices 2...3):
# Missing 'a' so is_valid() returns False!
# The while loop stops 
# Final result returned : 'abd'

# Time Complexity : O(N + K) - both pointers traverse string N at most once, and checking char counts takes constant time
# Space Complexity : O(1) - frequencies are tracked for lowercase English letters only : at most 26