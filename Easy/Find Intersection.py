# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: 
# the first element will represent a list of comma-separated numbers sorted in ascending order, 
# the second element will represent a second list of comma-separated numbers (also sorted). 
# Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. 
# If there is no intersection, return the string false.

def FindIntersection(strArr):
  # strArr is an array of strings sorted with [list1, list2]
  # List1 => comma separated numbers sorted in ascending order
  # List2 => comman separated numbers sorted in ascending order
  # Goal : Return a Comma Separated String containing numbers that occur in intersection of both

  # split(',') - chops a single long string into a list of pieces wherever it sees a comma.
  # strip() -   wipes away any accidental blank spaces from the front or back of a piece of text.
  # map() -  automatically runs a tool (like strip) on every single item in a collection.
  # list() - collects all  pieces and packs them neatly together into a fresh, usable list.
  
  # Split the string by comma and use map() to clean off any whitespace
  strArr1 = list(map(str.strip, strArr[0].split(",")))
  strArr2 = list(map(str.strip, strArr[1].split(",")))

  # Convert list into sets
  set1 = set(strArr1)
  set2 = set(strArr2)

  # Find common elements using intersection
  common_elements = set1 & set2

  # If the set is empty, return the string 'False'
  if not common_elements:
    return 'false'

  # sorted(..., key=int) converts the text pieces into numbers in numerical order and sorts.
  # ",".join(...) links all those sorted pieces together into a single text string with comma.

  # Sort the results and join them back with comma
  sorted_matches = sorted(list(common_elements), key = int)
  return ",".join(sorted_matches)

import sys
# Coderbyte passes the string via standard input; this approach handles both environments
raw_input = input()
if raw_input.startswith('[') and raw_input.endswith(']'):
    try:
        # If it evaluates to a list natively
        parsed_input = eval(raw_input)
    except:
        # Otherwise, manually split it safely
        parsed_input = [s.strip() for s in raw_input.strip('[]').split('", "')]
else:
    parsed_input = [raw_input]

print(FindIntersection(parsed_input))