# Reverse the order of words in a sentence (not the letters).
# Example  "hello there world" → "world there hello"

def reversetheword(strArr):
    newword = strArr.split(" ")
    newword.reverse()
    return " ".join(newword)
    
userword = input("Enter a string:")
print(reversetheword(userword))

# Time Complexity : O(N) Splitting, Reversing and Joining take constant time
# Space Complexity : O(N) because split creates a new list storing all the words in memory