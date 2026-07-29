# Return the count of vowels and consonants as a pair.
# Example  "delivery" → (3, 5)

def countvowelandconsonant(strArr):
    # make variables to track vowels and consonants
    vowels = 0
    consonants = 0
    vowel_set = 'aeiou'
    
    for char in strArr.lower():         # Convert to lowecase to handle uppercase
        if char.isalpha():              # Ensure it is a letter (ignore letters, symbols and other characters)
            if char in vowel_set:
                vowels = vowels + 1
            else:
                consonants = consonants + 1
    
    # Return the two counts (vowels,consonants) as pair
    return (vowels,consonants)

userword = input('Enter a String:')
print(countvowelandconsonant(userword))