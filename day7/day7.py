import re  # Import the regular expression module to extract numbers from the lines

# Define a recursive function to check if a number can be achieved by multiplying or adding numbers from the list
def find_number(numbers, index, current): 
    # Base case: if we've gone through all the numbers in the list
    if index == len(numbers): 
        # If the current value matches the first number in the list, return True
        if current == numbers[0]: 
            return True 
        else: 
            return False
    
    # Recursive case: Check both adding and multiplying the current number to the result
    return find_number(numbers, index + 1, current * numbers[index]) + find_number(numbers, index + 1, current + numbers[index])

# Open the file "long.txt" in read mode
with open("long.txt", "r") as file: 
    result = 0  # Initialize the result variable to accumulate the final answer
    
    # Iterate through each line in the file
    for line in file: 
        # Use a regular expression to find all sequences of digits in the line
        numbers = re.findall(r"\d+", line)
        
        # Convert the list of number strings into integers
        numbers = [int(x) for x in numbers]
        
        # If the list has 1 or fewer numbers, skip this line (no computation possible)
        if len(numbers) <= 1: 
            continue 
        
        # Call the recursive function `find_number` to check if a valid result can be found
        # We start at index 2 and pass the second number as the initial value for the recursive search
        elif find_number(numbers, 2, numbers[1]): 
            # If a valid result is found, add the first number in the list (which seems to be a key or target) to the result
            result += numbers[0]

    # Print the final result
    print(result)
