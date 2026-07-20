# Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero, 
# and return the number of valid combinations that can be formed with num pairs of parentheses. 
# For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis, 
# namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()). There are 5 total combinations when the input is 3, 
# so your program should return 5.


# Breaking down the question -
# num will have a pairs of opening bracket '(' and a closing bracket ')'
# num is an integer >= 0
# we need to return the number of valid combinations that can be formed with num pairs

  # Input : 3 means 3 opening brackets + 3 closing brackets
  # Pair 1 : () () ()
  # Pair 2 : () ( () )
  # Pair 3 : ( () ) ()
  # Pair 4 : ( ( () ) )
  # Pair 5 : ( () () )

  # Input : 2 means 2 opening and 2 closing brackets
  # Pair 1 : () ()
  # Pair 2 : ( () )
  
  # Intuition : 
  # Visualizing the "Backtrack"
  # Imagine a tree of choices. At the start, my string is empty "".
  # I can add ( -> so now the string becomes string (
  # I can choose to add another ( or a )
  # The code explores one choice all the way to the end.
  # Once it hits a dead end or a success, it backtracks (steps backward) to the previous choice and tries the other option.

def BracketCombinations(num):
    # A list to store every combination we find
    result = []
 
    # current : The Paranthesis String we are building
    # open_count : How many opening brackets '(' we have used
    # close_count : How many closing brackets ')' we have used
 
    def backtrack(current, open_count, close_count):
     
        # If string has all the parantheses (closing bracket + opening bracket), then we have found a pair or combination.
        # By this, if my num = 3 pairs, then we will have 2 * num = 6 brackets in total
        # Backtracking will help us to try every 6 bracket combination, while following all the rules of making a pair
        # To make a complete combination, the string I want to build right now (aka current's length) should match total number of brackets
        # Then, we can save it to result list
     
        if len(current) == 2 * num: 
            result.append(current)
            return
     
        # Add an opening bracket : It should be equal to num, right? because 6 brackets will form 3 pairs of each opening and closing brackets
        # Can we place a opening bracket ( now?
        # I will check my existing paranthesis pattern and add an opening bracket '(' onto the very end of it.
        # So, if my string was "(()" it will become "(()("
        # I just added a opening counter --> so I need to increment the count of my opening bracket
        # I did not change my closing bracket ---> so it is gonna remain the same
        if open_count < num:
            backtrack(current + "(", open_count + 1, close_count)
         
        # To make a valid combination, I need the closing brackets too
        # I can add a closing bracket, only if I have more opening brackets than my closing bracket
        if close_count < open_count:
            # Added + 1 to close_count because we are adding a closing bracket
            backtrack(current + ")", open_count, close_count + 1)
    
    # We should start with an empty string
    backtrack("",0,0)

    # Return how many valid combinations we found
    return len(result)

print(BracketCombinations(3))
     