"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        number = int(input("Input"))
        pass
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = number % 2 == 0
    odd_numbers = number % 2 != 0
    
    # Calculate average
    average = max[number] / min[number]
    
    
    # Numbers greater than average
    above_average = average + 1
    print(f"Min: {min(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Even number : ", even_numbers)
    print(f"Odd number : ", odd_numbers)
    print(f"Average : ", average)
    print(f"Above average", above_average)

if __name__ == "__main__":
    number_operations()