# Repeatedly sum the digits of a number until a single digit remains.
# Example  9875 → 2

def get_digit_sum(number):
    """
    Take a single integer and return the sum of its digits using
    pure mathematical operations (modulo and floor dvision)"""
    current_sum = 0
    temp_number = number
    
    # Process digits from right to left
    # while number is positive
    while temp_number > 0:
        last_digit = temp_number % 10   # Extract the last digit
        current_sum = current_sum + last_digit # Add it to the total
        temp_number = temp_number // 10  # Remove the last digit
    
    return current_sum

def digitalroot(nums):
    """
    Main Function : Repeatedly calls get_digit_sum until a single-digit remains
    """
    # Handle negative numbers by converting them to positive : take absolute value
    nums = abs(nums)
    
    # Base Case : 0 has a digital root of 0
    if nums == 0:
        return 0
    
    # Outer loop continues until 'nums' is reduced to a single digit (0-9)
    step_counter = 1
    # while nums is larger than 10
    while nums >= 10:
        previous_value = nums
        nums = get_digit_sum(nums)
        print(f"Step {step_counter}: Summed digit of {previous_value} to get {nums}")
        step_counter = step_counter + 1
    
    return nums

# Main Program Execution
if __name__ == "__main__":
    try:
        user_input_str = input("Enter a positive integer:")
        usernumber = int(user_input_str)
            
        print("\n----Digital Root Calculation Process----")
        final_result = digitalroot(usernumber)
        print("---------------------------------------")
        print(f"Final Digital Root: {final_result}")
    except ValueError:
        print("Error: Invalid Input! Please enter a valid number")
        