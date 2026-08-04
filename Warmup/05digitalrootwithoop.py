# Solving Digital Root Problem with OOPs
class DigitalRootCalculator:
    """
    Defining a class to calculate the digital root of numbers while maintaining a log of the 
    intermediate steps.
    """
    
    def __init__(self, initial_number: int):
        self.initial_number = abs(initial_number)
        self.history = []
    
    def _sum_digits(self, val:int) -> int:
        """ Sums the individual digits of a number """
        return sum(int(digit) for digit in str(val))
    
    def compute(self) -> int:
        """ Calculates the digital root and stores every step in self.history"""
        current_val = self.initial_number
        self.history.append(current_val)
        
        while current_val >= 10:
            current_val = self._sum_digits(current_val)
            self.history.append(current_val)
            
        return current_val
    
    def display_report(self):
        """ Prints a visual step-by-step breakdown of the calculation. """
        result = self.compute()
        
        print("\n" + "=" * 35)
        print(f" Digital Root Report for: {self.initial_number}")
        print("=" * 35)
        
        if len(self.history) == 1:
            print(f"Number is already a single digit: {result}")
        else:
            print("Transformation Sequence:")
            for index, val in enumerate(self.history):
                if index == len(self.history) - 1:
                    print(f" Final ==> {val}")
                else:
                    print(f" Step {index + 1}: {val} (Summing digits....)")
        
        print("=" * 35)
        print(f"Digital Root = {result} \n")
    

   def get_valid_integer():
        """ Prompts the user repeatedly until a valid integer is entered. """
        while True:
            raw_input = input("Enter a number to process: ")
            try: 
                return int(raw_input)
            except ValueError:
                print("Invalid input! Please enter digits only. \n")

# Main Execution Loop
if __name__ == "__main__":
    user_num = get_valid_integer()
    calculator = DigitalRootCalculator(user_num)
    calculator.display_report()