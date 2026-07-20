# Codeland Username Validation
# Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.

# If the username is valid then your program should return the string true, otherwise return the string false.
import re

def CodelandUsernameValidation(strParam):
    
    # Regular expression:
    # ^  -> start of the string
    # [A-Za-z0-9_]+ -> one or more letters, numbers, or underscores
    # $  -> end of the string
    p = "^[A-Za-z0-9_]+$"
    
    # Check whether the entire username matches the pattern
    res = bool(re.match(p,strParam))
       
    # Conditions:
    # 1. Length is between 4 and 25 characters
    # 2. First character is a letter
    # 3. Username contains only letters, numbers, and underscores
    # 4. Username does not end with an underscore
    
    if ( len(strParam) >=4 and len(strParam) <= 25 and strParam[0].isalpha() and res and strParam[-1] != '_') :
        return 'true'
    else:
        return 'false'
    
print(CodelandUsernameValidation('Shruti'))
