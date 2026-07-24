# Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. 
# If there are two or more words that are the same length, return the first word from the string with that length. 
# Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

import re

def LongestWord(sen):
    # Remove everything that is not a letter
    clean_sentence = re.sub(r'[^\w\s]', '', sen)
    
    # Split into a list of words
    words = clean_sentence.split()
    
    # Sort in place by length descending
    words.sort(key = len, reverse = True)
  
    return words[0]

# keep this function call here 
print(LongestWord(input()))

# As we are using Sorting here
# Time Complexity : O(NlogN) : Cleaning and Splitting take O(N) + Sorting O(NlogN)
# Space Complexity : O(N) : Storing list words takes O(N) memory